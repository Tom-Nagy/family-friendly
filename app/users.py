from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from bson.objectid import ObjectId
from app import mongo
from app.classes.user_class import User
from app.validators.validators import validate_passwords

users = Blueprint("users", __name__)

# Collection
users_coll = mongo.db.users


# Route for signing up
@users.route("/signup", methods=["GET", "POST"])
def signup():
    # POST method
    if request.method == "POST":

        pass1 = request.form.get("password")
        pass2 = request.form.get("conf_password")

        if validate_passwords(pass1, pass2):
            # Create an instance of User with the form input fields
            new_user = User(**request.form)

            # Insert to the database
            new_user.insert_user_to_db()

            # Put the new user into session cookie
            session["user"] = new_user.username

            # Feedback message
            flash(f"Well done {session['user']} and Welcome to the Family.")
            return redirect(url_for("users.profile"))

        else:
            flash("Passwords must match, Please enter valid passwords.")
            return redirect(url_for("users.signup"))
    
    # Default GET method
    return render_template("signup.html")


@users.route("/profile")
def profile():
    return render_template("profile.html")
