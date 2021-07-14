"""
Views related to the presentation of the website,
home page
"""
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
# from app.flashes.flash_messages import *

# method that utilise the whole class,
# can be use on the class without the object instantiated to begin with.


main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")