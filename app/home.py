"""
Views related to the presentation of the website,
home page
"""
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/home")
def home():
    return render_template("home.html")