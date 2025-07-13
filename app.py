from flask import Flask, render_template, request, redirect, Response, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/recommend_page")
# def recommend_page():
#     return render_template("recommend_page.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)