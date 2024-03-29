"""
Views related to the creation of events
"""
# Imports
from app import mongo
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
from bson.objectid import ObjectId
from app.classes.user_class import User
from app.classes.event_class import Event
from app.flashes.flash_messages import EventsMsg

# Blueprint
events = Blueprint("events", __name__)

# Collection
users_coll = mongo.db.users
events_coll = mongo.db.events


@events.route("/browse_events", methods=["GET", "POST"])
def browse_events():
    # Check if the user is logged in.
    if session:
        user = User.get_one_user_coll(session['user'])
        # Get all the events to display
        events_list = Event.get_all_events()
        return render_template(
            "events.html", events_list=events_list, user=user)

    # Get all the events to display
    events_list = Event.get_all_events()
    return render_template("events.html", events_list=events_list)


@events.route("/search_events", methods=["GET", "POST"])
def search_events():
    # Check if the user is logged in.
    if session:
        user = User.get_one_user_coll(session['user'])
        # Get the search from the form
        query = request.form.get("query_search_events")
        # Get some events to display
        events_list = list(events_coll.find({"$text": {"$search": query}}))
        return render_template(
            "events.html", events_list=events_list, user=user)

    # Get the search from the form
    query = request.form.get("query_search_events")
    # Get some events to display
    events_list = list(events_coll.find({"$text": {"$search": query}}))
    return render_template("events.html", events_list=events_list)


@events.route("/select_events", methods=["GET", "POST"])
def select_events():
    # Check if the user is logged in.
    if session:
        user = User.get_one_user_coll(session['user'])
        # Get the category selected
        category = request.form.get("event_category")
        # Set the field to search on
        field = "event_category"
        # Get some events to display
        events_list = Event.get_some_events(field, category)
        return render_template(
            "events.html", events_list=events_list, user=user)

    # Get the category selected
    category = request.form.get("event_category")
    # Set the field to search on
    field = "event_category"
    # Get some events to display
    events_list = Event.get_some_events(field, category)
    return render_template("events.html", events_list=events_list)


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
            User.append_info_to_user((get_attr, event_id), user_id)

            flash(EventsMsg.event_created)
            return redirect(url_for('users.profile', username=session["user"]))

    # Check if user is logged in and if session's user correspond to username
    if session["user"] and session["user"] == username:
        # Get user from the db and return a user collection
        user = User.get_one_user_coll(username)
        return render_template('create_event.html', user=user)
    else:
        return redirect(url_for('index.home'))


@events.route("/see_event", methods=["GET", "POST"])
def see_event():
    # Check if the user is logged in.
    if session:
        user = User.get_one_user_coll(session["user"])
        # Get the event_id passed by the form from browse_events
        # to display the relevant event
        event_id = request.form.get("event_id")
        event = Event.get_one_event(event_id)
        return render_template("see_event.html", event=event, user=user)


@events.route("/update_event", methods=["GET", "POST"])
def update_event():

    user = User.get_one_user_coll(session['user'])
    event_id = request.form.get("update_event")
    event = Event.get_one_event(event_id)
    return render_template("update_event.html", event=event, user=user)


@events.route("/updated_event/<event_id>", methods=["GET", "POST"])
def updated_event(event_id):
    if request.method == "POST":
        # Create a dic with new values from the form
        new_info = {
            "event_category": request.form.get("event_category"),
            "event_location": request.form.get("event_location"),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_age_range": request.form.get("event_age_range"),
            "event_description": request.form.get("event_description")
        }

        # Add new info to db
        Event.update_event(new_info, event_id)

        # Get all the events to display
        events_list = Event.get_all_events()
        return redirect(url_for(
            'events.browse_events', events_list=events_list))


@events.route("/cancel_event/<username>", methods=["GET", "POST"])
def cancel_event(username):
    if session["user"] and session["user"] == username:
        # Get the event id from the form
        event_id = request.form.get("cancel_event")

        # Delete event from the event collection in db
        Event.delete_event(event_id)

        # Get the user id from the db
        user_id = User.get_one_user_coll(username)["_id"]
        # Set the attribute to update in the user doc
        get_user_attr = "events_created"
        # Delete event_id from corresponding field of the user
        User.remove_info_from_user_list((get_user_attr, event_id), user_id)

        # get all user from db
        all_users = users_coll.find()
        # Check if user has joined the event and if so remove the event
        # from his document
        for user in all_users:
            # Set the attribute to update in the user doc
            get_user_attr = "events_joined"

            if event_id in user[get_user_attr]:
                # Get the corresponding user id from the db
                user_id = user["_id"]
                # Delete event_id from corresponding field of the user
                User.remove_info_from_user_list(
                    (get_user_attr, event_id), user_id)

        flash(EventsMsg.event_deleted)

        user = User.get_one_user_coll(session['user'])
        events_list = Event.get_all_events()
        return render_template(
            "events.html", events_list=events_list, user=user)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))


@events.route("/join_event/<username>", methods=["GET", "POST"])
def join_event(username):
    if session["user"] and session["user"] == username:
        # Get the event id from the form
        event_id = request.form.get("join_event")

        # Get the user id from the db
        user = User.get_one_user_coll(username)
        user_id = user["_id"]

        # Set the attribute to update in the user doc
        get_user_attr = "events_joined"
        # Add the event id to the corresponding user field
        User.append_info_to_user((get_user_attr, event_id), user_id)

        # Set the attribute to update in the event doc
        get_event_attr = "event_joined_by"
        # Add the user id to the corresponding event field
        Event.append_info_to_event((get_event_attr, user_id), event_id)

        flash(EventsMsg.event_joined)

        events_list = Event.get_all_events()
        return render_template(
            "events.html", events_list=events_list, user=user)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))


@events.route("/leave_event/<username>", methods=["GET", "POST"])
def leave_event(username):
    if session["user"] and session["user"] == username:
        # Get the event id from the form
        event_id = request.form.get("leave_event")

        # Get the user id from the db
        user = User.get_one_user_coll(username)
        user_id = user["_id"]

        # Set the attribute to update in the user doc
        get_user_attr = "events_joined"
        # Delete the event id from the corresponding user field
        User.remove_info_from_user_list((get_user_attr, event_id), user_id)

        # Set the attribute to update in the event doc
        get_event_attr = "event_joined_by"
        # Delete the user id from the corresponding event field
        Event.remove_info_from_event_list((get_event_attr, user_id), event_id)

        flash(EventsMsg.event_left)

        events_list = Event.get_all_events()
        return render_template(
            "events.html", events_list=events_list, user=user)

    else:
        flash(EventsMsg.didnt_work)
        return redirect(url_for('index.home'))


@events.route("/like_event/<username>", methods=["GET", "POST"])
def like_event(username):
    if request.method == "POST":
        user = User.get_one_user_coll(username)
        user_id = user["_id"]
        event_id = request.form.get("like_event")

        if str(event_id) not in user["events_liked"]:
            # Add the like to event_likes field in db
            Event.append_info_to_event(("event_likes", user_id), event_id)
            # Add the event to events_liked field in db
            User.append_info_to_user(("events_liked", event_id), user_id)

            # Refresh see_event.html
            event = Event.get_one_event(event_id)
            user = User.get_one_user_coll(username)

            return render_template('see_event.html', event=event, user=user)

        return redirect(url_for("events.browse_events"))


@events.route("/unlike_event/<username>", methods=["GET", "POST"])
def unlike_event(username):
    if request.method == "POST":
        user = User.get_one_user_coll(username)
        user_id = user["_id"]
        event_id = request.form.get("unlike_event")

        if str(event_id) in user["events_liked"]:

            # Remove the like to event_likes field in db
            Event.remove_info_from_event_list(
                ("event_likes", user_id), event_id)
            # Remove the event to events_liked field in db
            User.remove_info_from_user_list(
                ("events_liked", event_id), user_id)

            # Refresh see_event.html
            event = Event.get_one_event(event_id)
            user = User.get_one_user_coll(username)
            return render_template('see_event.html', event=event, user=user)

        return redirect(url_for("events.browse_events"))
