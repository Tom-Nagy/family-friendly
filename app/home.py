"""
Views related to the presentation of the website,
home page
"""
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from app.classes.user_class import User

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/home")
def home():
    if session['user']:
        user = User.get_one_user_coll(session['user'])
        return render_template("home.html", user=user)
    return render_template("home.html")
