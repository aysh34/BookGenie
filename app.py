from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "superkey"

# ========== Load Models Safely ==========
try:
    top_50 = pickle.load(open("Models/top_50.pkl", "rb"))
    filtered_books = pickle.load(open("Models/filtered_books.pkl", "rb"))
    similarity = pickle.load(open("Models/similarity.pkl", "rb"))
    final_df = pickle.load(open("Models/final_df.pkl", "rb"))
except Exception as e:
    print(f"[ERROR] Failed to load models: {e}")
    top_50 = filtered_books = similarity = final_df = None


# ========== Context Processor ==========
@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


# ========== Routes ==========


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/trending")
def trending():
    if top_50 is None:
        flash("Error loading trending books. Please try again later.", "danger")
        return redirect(url_for("index"))
    books = top_50.to_dict(orient="records")
    return render_template("trending.html", books=books)


@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    user_input = request.form.get("user_input")

    if not user_input:
        flash("Please enter a book title.", "warning")
        return redirect(url_for("recommend"))

    if final_df is None or user_input not in final_df.index:
        flash(f"'{user_input}' not found. Try another title.", "warning")
        return redirect(url_for("recommend"))

    try:
        if similarity is None:
            flash(
                "Recommendation system is currently unavailable. Please try again later.",
                "danger",
            )
            return redirect(url_for("recommend"))

        index = int(np.where(final_df.index == user_input)[0][0])
        sorted_similarity_scores = sorted(
            list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True
        )[1:6]

        recommendations = []

        if filtered_books is None:
            flash(
                "Recommendation system is currently unavailable. Please try again later.",
                "danger",
            )
            return redirect(url_for("recommend"))

        for i in sorted_similarity_scores:
            temp_df = filtered_books[
                filtered_books["Book-Title"] == final_df.index[i[0]]
            ]
            temp_df = temp_df.drop_duplicates("Book-Title")

            if not temp_df.empty:
                recommendations.append(
                    {
                        "title": temp_df["Book-Title"].values[0],
                        "author": temp_df["Book-Author"].values[0],
                        "image": temp_df["Image-URL-L"].values[0],
                    }
                )

        if not recommendations:
            flash("Sorry, no recommendations could be generated.", "info")

        return render_template("recommend.html", recommendations=recommendations)

    except Exception as e:
        print(f"[ERROR] Recommendation failed: {e}")
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for("recommend"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
