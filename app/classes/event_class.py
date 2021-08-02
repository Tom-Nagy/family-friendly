"""
Class build to perform CRUD operation on events collection
"""
# import
from app import mongo
from flask import Flask, request
from bson.objectid import ObjectId

# collection
events_coll = mongo.db.events
users_coll = mongo.db.users


class Event:
    """
    Class that Creates an instance of event,
    Prepares the data for the database and
    Inserts/Delete/Update the data in the events collection.
    """

    # Create an Event object
    def __init__(self, event_category, event_location, event_age_range,
                 event_date, event_time, event_description, _id=None,
                 event_created_by=None, event_likes=None,
                 event_joined_by=None):
        """
        Initialisation of Event, setting attributes value to None 
        as placeholder for future input. 
        """
        self._id = _id
        self.event_category = event_category
        self.event_location = event_location
        self.event_age_range = event_age_range
        self.event_date = event_date
        self.event_time = event_time
        self.event_description = event_description
        self.event_created_by = ObjectId(
            event_created_by) if not None else 'null'
        self.event_likes = [event_likes] if not None else 'null'
        self.event_joined_by = [event_joined_by] if not None else 'null'

    # method used as a formatter
    def event_info_to_dic(self):
        """
        Format Event attributes to a dictionary in order to prepare data
        to be inserted to the database.
        """
        event_info = {
            'event_category': self.event_category,
            'event_location': self.event_location,
            'event_age_range': self.event_age_range,
            'event_date': self.event_date,
            'event_time': self.event_time,
            'event_description': self.event_description,
            'event_created_by': self.event_created_by,
            'event_joined_by': self.event_joined_by,
            'event_likes': self.event_likes
        }
        return event_info

    # Add Event to the database
    def insert_event_to_db(self):
        """
        Use event_info dic generated by event_info_to_dic()
        as data to insert into the db.
        """
        try:
            events_coll.insert_one(self.event_info_to_dic())
        except Exception as e:
            print(e)

    # method that use the whole class,
    # can be use on the class without the object instantiated to begin with.
    @classmethod
    def get_all_events(cls):
        """
        Get the events from the db as a list,
        Return a list of Event instances.
        """
        try:
            events = list(events_coll.find())
            events_list = []
            if events is not None:
                for event in events:
                    one_event = cls(**event)
                    events_list.append(one_event)
            return events_list
        except Exception as e:
            print(e)

    @classmethod
    def get_some_events(cls, field, filter):
        """
        Takes two param of field and filter;
        Get the corresponding events from the db,
        Return a list of Event instances.
        """
        try:
            events = list(events_coll.find({field: filter}))
            events_list = []
            if events is not None:
                for event in events:
                    one_event = cls(**event)
                    events_list.append(one_event)
            return events_list
        except Exception as e:
            print(e)

    @classmethod
    def get_events_joined(cls, user_id):

        try:
            user = users_coll.find_one({"_id": ObjectId(user_id)})
            events = list(events_coll.find())
            events_list = []
            if events is not None:
                for event in events:
                    if str(event["_id"]) in user["events_joined"]:
                        one_event = cls(**event)
                        events_list.append(one_event)
            return events_list

        except Exception as e:
            print(e)

    @classmethod
    def get_one_event(cls, event_id):
        """
        Takes the event_id as param,
        Return an instance of this event.
        """
        try:
            event = events_coll.find_one({"_id": ObjectId(event_id)})
            return cls(**event)
        except Exception as e:
            print(e)

    @classmethod
    def get_last_event_crated_by_user(cls, user_id):
        """
        Takes the ObjectId of the creator as param,
        Return an instance of the last event created by this user from the db.
        """
        try:
            # Credit for the sorting part of the code to Neil Lunn
            # from stackoverflow (https://stackoverflow.com/questions/49871030/how-fetch-latest-records-using-find-one-in-pymongo)
            event = events_coll.find_one(
                {"event_created_by": ObjectId(user_id)}, sort=[('_id', -1)])
            return cls(**event)
        except Exception as e:
            print(e)

    @staticmethod
    def append_info_to_event(new_value, event_id):
        """
        Takes a tuple (of field/attr and user id), and event_id as param;
        Append new info,
        Update db
        """
        # unpack the tuple
        (get_attr, user_id) = new_value
        try:
            # get the user and corresponding attr/key and append the new value
            event = events_coll.find_one({"_id": ObjectId(event_id)})
            corresponding_list = event[get_attr]
            obj_id = str(ObjectId(user_id))

            if isinstance(corresponding_list, list):
                corresponding_list.append(obj_id)
                new_list = {get_attr: corresponding_list}
                events_coll.update_one({'_id': ObjectId(event_id)},
                                       {'$set': new_list})
            else:
                corresponding_list = []
                corresponding_list.append(obj_id)
                new_list = {get_attr: corresponding_list}
                events_coll.update_one({'_id': ObjectId(event_id)},
                                       {'$set': new_list})
        except Exception as e:
            print(e)

    @staticmethod
    def remove_info_from_event_list(details, event_id):
        """
        Takes a tuple (of field/attr and user_id), and event_id as param;
        Delete info with given details,
        Update db
        """
        # unpack the tuple
        (get_attr, user_id) = details
        try:
            # get the event and corresponding attr/key
            event = events_coll.find_one({"_id": ObjectId(event_id)})
            corresponding_list = event[get_attr]
            obj_id = str(ObjectId(user_id))

            # remove user_id from list
            corresponding_list.remove(obj_id)

            # Update db
            new_list = {get_attr: corresponding_list}
            events_coll.update_one({'_id': ObjectId(event_id)},
                                   {'$set': new_list})
        except Exception as e:
            print(e)

    @staticmethod
    def delete_event(event_id):
        """
        Delete an event from the db,
        Takes an event _id as parameter. 
        """
        try:
            events_coll.delete_one({"_id": ObjectId(event_id)})
        except Exception as e:
            print(e)
