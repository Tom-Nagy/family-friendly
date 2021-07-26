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
        # Get the event_id passed by the form from browse_events
        # to display the relevant event
        event_id = request.form.get("event_id")
        event = Event.get_one_event(event_id)
        print(type(event._id))
        print(type(user["events_joined"]))
        return render_template("see_event.html", event=event, user=user)


@events.route("/cancel_event/<username>", methods=["GET", "POST"])
def cancel_event(username):
    if session["user"] and session["user"] == username:
        # Get the event id from the form
        event_id = request.form.get("cancel_event")
        # Delete event from the event collection in db
        Event.delete_event(event_id)
        flash(EventsMsg.event_deleted)

        events_list = Event.get_all_events()
        return render_template("events.html", events_list=events_list)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))


@events.route("/join_event/<username>", methods=["GET", "POST"])
def join_event(username):
    if session["user"] and session["user"] == username:
        # Get the event id from the form
        event_id = request.form.get("join_event")

        # Get the user id from the db
        user_id = User.get_one_user_coll(username)["_id"]
        
        # Set the attribute to update to the user doc
        get_user_attr = "events_joined"
        # Add the event id to the corresponding user attribute
        User.append_user_info((get_user_attr, event_id), user_id)

        # Set the attribute to update to the event doc
        get_event_attr = "event_joined_by"
        # Add the user id to the corresponding event attribute
        Event.append_event_info((get_event_attr, user_id), event_id)

        flash(EventsMsg.event_joined)

        events_list = Event.get_all_events()
        return render_template("events.html", events_list=events_list)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))
