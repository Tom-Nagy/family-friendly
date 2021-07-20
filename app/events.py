"""
Views related to the creation of events
"""
# Imports
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from app.classes.user_class import User
from app.classes.event_class import Event
from app.flashes.flash_messages import EventsMsg

# Blueprint
events = Blueprint("events", __name__)

@events.route("/create_event/<username>", methods=["GET", "POST"])
def create_event(username):
    if request.method == "POST":
        user = User.get_one_user_coll(username)
        new_event = Event(**request.form)
        Event.insert_event_to_db(new_event)

        flash(EventsMsg.event_created)
        return redirect(url_for('users.profile', username=session["user"]))

    # Check if user is logged in and if session's user correspond to username
    if session["user"] and session["user"] == username:
        # Get user from the db and return a user collection
        user = User.get_one_user_coll(username)
        return render_template('create_event.html', user=user)
    else:
        return redirect(url_for('index.home'))


@events.route("/browse_events", methods=["GET", "POST"])
def browse_events():
    if session["user"]:
        user = User.get_one_user_coll(session["user"])
        events_list = Event.get_all_events()
        return render_template("events.html", events_list=events_list, user=user)
    else:
        events_list = Event.get_all_events()
        return render_template("events.html", events_list=events_list)