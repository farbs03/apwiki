from main.models import User, Post
from main.organized_classes import filtered_classes, subjects
from flask import render_template, redirect, flash, url_for
from main import app
from main.forms import RegistrationForm, LoginForm

classes = filtered_classes
subject_list = subjects

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'difficulty': 5,
        'value': 5
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'difficulty': 3,
        'value': 4
    }
]
totalDiffs = 0
totalValues = 0
totalDiff = 0
totalValue = 0

for i in posts:
	totalDiffs += 1
	totalValues += 1
	totalDiff += i["difficulty"]
	totalValue += i["value"]

averageDiff = totalDiff / totalDiffs
averageValue = totalValue / totalValues

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/courses")
def courses():
	return render_template("courses.html", classes=classes, subjects=subject_list)

@app.route("/course/<some_course>")
def course(some_course):
	for course in classes:
		if course["name"] == some_course:
			return render_template("course.html", course=course, posts=posts, averageValue = averageValue, averageDiff = averageDiff)
	return render_template('404.html')

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created for {form.name.data}!", 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "farbechr000@hsestudents.org" and form.password.data == "Hse220793":
			flash('You have been logged in!', "success")
			return redirect(url_for('home'))
		else:
			flash('Login unsucessful, please check email and password', "danger")
	return render_template("login.html", form=form)

@app.route("/user")
def user():
	return render_template('user.html')