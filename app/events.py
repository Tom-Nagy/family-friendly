"""
Views related to the creation of events
"""
# Imports
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from bson.objectid import ObjectId
from app.classes.user_class import User
from app.classes.event_class import Event
from app.flashes.flash_messages import EventsMsg

# Blueprint
events = Blueprint("events", __name__)


@events.route("/create_event/<username>", methods=["GET", "POST"])
def create_event(username):
    if request.method == "POST":
        # Add event to db
        new_event = Event(**request.form)
        Event.insert_event_to_db(new_event)

        # Update user info with event_created
        user = User.get_one_user_coll(username)
        user_id = user["_id"]
        get_attr = "events_created"

        # Create an Istance of the new event to get its id
        event_created = Event.get_last_event_crated_by_user(user_id)
        if event_created:
            event_id = event_created._id
            # Update user info
            User.append_user_info((get_attr, event_id), user_id)

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
    
    # Get all the events to display in a carousel
    events_list = Event.get_all_events()
    return render_template("events.html", events_list=events_list)


@events.route("/see_event", methods=["GET", "POST"])
def see_event():
    # Check if user is logged in
    if session["user"]:
        user = User.get_one_user_coll(session["user"])

        if request.method == "POST": 
            event_id = request.form.get("event_id")
            event = Event.get_one_event(event_id)
            return render_template("see_event.html", event=event, user=user)


@events.route("/cancel_event/<username>", methods=["GET", "POST"])
def cancel_event(username):
    if session["user"] and session["user"] == username:
        if request.method == "Post":
            event_id = request.form.get("cancel_event")
            Event.delete_event(event_id)
            flash(EventsMsg.event_deleted)

            user = User.get_one_user_coll(session["user"])
            events_list = Event.get_all_events()
            return render_template("events.html", events_list=events_list, user=user)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))
