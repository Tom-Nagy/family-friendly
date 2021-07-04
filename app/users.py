from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from bson.objectid import ObjectId
from app import mongo

users = Blueprint("users", __name__)

# Collection
users_coll = mongo.db.users

### Shoud be for signup login profile...

@users.route("/")
@users.route("/signup")
def signup():
    
    return render_template("signup.html")