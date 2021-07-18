from flask import Flask, request
from flask.templating import render_template
from  flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "PopcornAndCats420"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_home():
    """shows the home page to pick a story template"""
    return render_template("home.html", stories=stories)

@app.route("/form/<int:id>")
def show_form(id):
    """shows form for selected template"""
    prompts = stories[id - 1].prompts
    return render_template("form.html", prompts=prompts, id=id)

@app.route("/story/<int:id>", methods=["POST"])
def show_story(id):
    """shows the madlib page"""
    answers = {key: val for key, val in dict(request.form).items()}
    text = stories[id - 1].generate(answers)
    return render_template("story.html", text=text)
