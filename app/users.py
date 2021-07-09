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


# Sign Up
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

# Log In
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

    # Check if user is logged in and if session's user correspond to username
    if session["user"] and session["user"] == username:

        # Get user from the db and return an instance of User
        user = User.get_one_user(username)
        return render_template("profile.html", user=user)

    return redirect(url_for("users.login"))


@users.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):

    if request.method == "POST":
        # Check if new info are valid
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        existing_email = User.check_if_email_exists(email)
        existing_username = User.check_if_username_exists(username)
        user = User.get_one_user_coll(session["user"])
        

        if existing_email and email != user.email:
            flash(email_exists)
            return redirect(url_for('users.update_profile', username=session['user']))

        if existing_username and username != user.username:
            flash(username_exists)
            return redirect(url_for('users.update_profile', username=session['user']))

        # Check if the password is correct

        if check_password_hash(user.password, password):
            # replace the curent values of the User instance and Add Updated info to db
            user.first_name = request.form.get("first_name")
            user.last_name = request.form.get("last_name")
            user.email = request.form.get("email")
            user.username = request.form.get("username")
            user.profile_picture = request.form.get("profile_picture")

            user.update_user()
            
            flash("Updated")
            return redirect(url_for('users.profile', username=session['user']))

        flash(incorrect_password)
        return redirect(url_for('users.update_profile', username=session['user']))

    # Check if user is logged in and if session's user correspond to username
    if session["user"] and session["user"] == username:
        user = User.get_one_user(username)
        return render_template("update_profile.html", user=user)

    return redirect(url_for("users.login"))


@users.route("/logout")
def logout():
    # Remove user from session cookie
    session.pop("user")
    flash(logged_out)
    return redirect(url_for('users.login'))
