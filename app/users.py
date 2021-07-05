from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from werkzeug.security import check_password_hash
from bson.objectid import ObjectId
from app import mongo
from app.flashes.flash_messages import *
from app.classes.user_class import User
from app.validators.validators import validate_passwords

users = Blueprint("users", __name__)

# Collection
users_coll = mongo.db.users


# Route for signing up
@users.route("/")
@users.route("/signup", methods=["GET", "POST"])
def signup():
    # POST method
    if request.method == "POST":

        # Check if username already exists
        username = request.form.get("username")
        if User.check_if_username_exists(username):
            flash(username_exists)
            return redirect(url_for('users.signup'))
        
        # Check if email already exists
        email = request.form.get("email")
        if User.check_if_email_exists(email):
            flash(email_exists)
            return redirect(url_for('users.signup'))

        # Check if the passwords are valid and match
        pass1 = request.form.get("password")
        pass2 = request.form.get("conf_password")

        if validate_passwords(pass1, pass2):
            # Create an instance of User with the form input fields
            new_user = User(**request.form)

            # Insert to the database
            new_user.insert_user_to_db()

            # Put the new user into session cookie
            session["user"] = new_user.username

            flash(signed_in)
            return redirect(url_for("users.profile", username=session["user"]))

        else:
            flash(invalid_passwords)
            return redirect(url_for("users.signup"))
    
    # Default GET method
    return render_template("signup.html")


@users.route("/login", methods=["Get", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user exists
        existing_user = User.check_if_email_exists(email)

        if existing_user:

            # Check if hashed password matches input password
            if check_password_hash(existing_user["password"], password):

                # Put user into session cookie
                session["user"] = existing_user["username"]
                flash(logged_in)
                return redirect(url_for('users.profile', username=session["user"]))

            else:
                flash(incorrect_details)
                return redirect(url_for('users.login'))

        else:
            flash(incorrect_details)
            return redirect(url_for('users.login'))

    return render_template("login.html")


@users.route("/profile/<username>")
def profile(username):

    # Get user from the db and return an instance of User
    user = User.get_one_user(username)

    # Check if user is logged in
    if session["user"] and session["user"] == username:
        return render_template("profile.html", user=user)

    return redirect(url_for("users.login"))
