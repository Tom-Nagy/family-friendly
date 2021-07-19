"""
Views related to the creation of events
"""

from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from app.classes.user_class import User
# from app.flashes.flash_messages import *

create = Blueprint("create", __name__)

@create.route("/create_event/<username>", methods=["GET", "POST"])
def create_event(username):

    # Check if user is logged in and if session's user correspond to username
    if session["user"]:
        # Get user from the db and return a user collection
        user = User.get_one_user_coll(username)
        return render_template('create_event.html', user=user)
    else:
        return redirect(url_for('index.home'))