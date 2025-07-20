from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import pickle
import os
import numpy as np
from difflib import get_close_matches

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "superkey")

# Global variables for models
top_50 = None
filtered_books = None
similarity = None
final_df = None


def load_models():
    """Load models on first request"""
    global top_50, filtered_books, similarity, final_df

    if top_50 is not None:
        return True

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(base_dir, "Models")

        top_50 = pickle.load(open(os.path.join(models_dir, "top_50.pkl"), "rb"))
        filtered_books = pickle.load(
            open(os.path.join(models_dir, "filtered_books.pkl"), "rb")
        )
        similarity = pickle.load(open(os.path.join(models_dir, "similarity.pkl"), "rb"))
        final_df = pickle.load(open(os.path.join(models_dir, "final_df.pkl"), "rb"))
        final_df.index = final_df.index.astype(str).str.strip()

        return True
    except Exception as e:
        print(f"[ERROR] Failed to load models: {e}")
        return False


# ========== Context Processor ==========
@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


# ========== Routes ==========

@app.route("/health")
def health():
    """Health check endpoint"""
    return {"status": "healthy", "message": "BookGenie is running!"}, 200

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error loading index page: {str(e)}", 500


@app.route("/debug")
def debug():
    """Debug endpoint to check file structure"""
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    debug_info = {
        "base_dir": base_dir,
        "files_in_base": os.listdir(base_dir) if os.path.exists(base_dir) else "Base dir not found",
        "templates_exists": os.path.exists(os.path.join(base_dir, "templates")),
        "models_exists": os.path.exists(os.path.join(base_dir, "Models")),
        "static_exists": os.path.exists(os.path.join(base_dir, "static"))
    }
    
    if os.path.exists(os.path.join(base_dir, "templates")):
        debug_info["templates_files"] = os.listdir(os.path.join(base_dir, "templates"))
    
    if os.path.exists(os.path.join(base_dir, "Models")):
        debug_info["model_files"] = os.listdir(os.path.join(base_dir, "Models"))
    
    return debug_info, 200

@app.route("/trending")
def trending():
    if not load_models():
        flash("Error loading trending books. Please try again later.", "danger")
        return redirect(url_for("index"))

    global top_50
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
        flash("Please enter a book name to get recommendations.", "warning")
        return redirect(url_for("recommend"))

    if not load_models():
        flash("Recommendation system is currently unavailable.", "danger")
        return redirect(url_for("recommend"))

    # At this point, models are loaded and not None
    global final_df, similarity, filtered_books

    if final_df is None or similarity is None or filtered_books is None:
        flash("Recommendation system is currently unavailable.", "danger")
        return redirect(url_for("recommend"))

    # === Fuzzy Matching ===
    all_titles = final_df.index.tolist()
    lower_titles = [title.lower() for title in all_titles]
    matches = get_close_matches(
        user_input.strip().lower(), lower_titles, n=1, cutoff=0.7
    )

    if not matches:
        flash(f"'{user_input}' not found. Try a different title.", "warning")
        return render_template("recommend.html", suggestions=all_titles[:10])

    # Get original casing of matched title
    matched_index = lower_titles.index(matches[0])
    matched_title = all_titles[matched_index]

    try:
        index = int(np.where(final_df.index == matched_title)[0][0])
        sorted_similarity_scores = sorted(
            list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True
        )[1:5]

        recommendations = []

        for i in sorted_similarity_scores:
            temp_df = filtered_books[
                filtered_books["Book-Title"] == final_df.index[i[0]]
            ].drop_duplicates("Book-Title")

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
