"""
Views related to the footer of the website,
presents on all pages.
"""
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from app.classes.user_class import User

footer = Blueprint("footer", __name__)


@footer.route("/contact/<username>", methods=["GET", "POST"])
def contact(username):
    user = User.get_one_user_coll(username)
    return render_template("contact.html", user=user)


@footer.route("/privacy-policy")
def privacy_policy():
    if session:
        user = User.get_one_user_coll(session['user'])
        return render_template("privacy_policy.html", user=user)
