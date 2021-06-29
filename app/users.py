from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from bson.objectid import ObjectId
from app import mongo

users = Blueprint("users", __name__)

# Collection
usersdb = mongo.db.users

### Shoud be for signup login profile...

@users.route("/")
@users.route("/home")
def home():
    users = mongo.db.users.find()
    return render_template("home.html", users=users)