import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# ---- CONFIG ----- #
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY_FLASK")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    all_recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=all_recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Check first if user already exists
        if existing_user:
            flash("Username already exists! Please try again.")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("users/register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Check if user already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("{}, Welcome back!".format(request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("users/login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        flash("You can add your favorite recipe here.")
        return render_template("users/profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "category_name": request.form.get("category_name"),
                "recipe_description": request.form.get("recipe_description"),
                "img_url": request.form.get("img_url"),
                "ingredients": request.form.get("ingredients"),
                "instructions": request.form.get("instructions"),
                "date_added": request.form.get("date_added"),
                "username": session["user"]
            }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipes Successfully Added")
        return redirect(url_for("get_recipes"))

    all_categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=all_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
