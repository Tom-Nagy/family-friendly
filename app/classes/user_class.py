"""
Class build to perform CRUD operation on users collection
"""
# Imports
from app import mongo
from flask import Flask, request
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import os

# Collections:
users_coll = mongo.db.users


class User:

    """
    Class that Creates an instance of a user,
    Prepares the data for the database and
    Inserts/Delete/Update the data in the users collection.
    """

    # Create a User object
    def __init__(self, first_name, last_name, username, email, password,
                conf_password=None, _id=None, profile_picture=None,
                events_joined=None, events_liked=None, questions_liked=None,
                answers_liked=None, contacts_liked=None, tips_liked=None,
                events_created=None, questions_created=None,
                answers_created=None, contacts_created=None,
                tips_created=None):
                """
                Initialisation of User, setting attributes value to None 
                as placeholder for future input.
                """
                self.first_name = first_name
                self.last_name = last_name
                self._id = _id
                self.username = username
                self.email = email
                self.password = generate_password_hash(password)
                self.profile_picture = profile_picture if not None else 'null'
                self.events_joined = [events_joined] if not None else ['null']
                self.events_liked = [events_liked] if not None else ['null']
                self.questions_liked = [questions_liked] if not None else ['null']
                self.answers_liked = [answers_liked] if not None else ['null']
                self.contacts_liked = [contacts_liked] if not None else ['null']
                self.tips_liked = [tips_liked] if not None else ['null']
                self.events_created = [events_created] if not None else ['null']
                self.questions_created = [questions_created] if not None else ['null']
                self.answers_created = [answers_created] if not None else ['null']
                self.contacts_created = [contacts_created] if not None else ['null']
                self.tips_created = [tips_created] if not None else ['null']

    # method used as a formatter   
    def user_info_to_dic(self):
        """
        Format User attributes to a dictionary in order to prepare data
        to be inserted to the database.
        """
        user_info = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_picture': self.profile_picture,
            'events_joined': self.events_joined,
            'events_liked': self.events_liked,
            'questions_liked': self.questions_liked,
            'answers_liked': self.answers_liked,
            'contacts_liked': self.contacts_liked,
            'tips_liked': self.tips_liked,
            'events_created': self.events_created,
            'questions_created': self.questions_created,
            'answers_created': self.answers_created,
            'contacts_created': self.contacts_created,
            'tips_created': self.tips_created,
        }
        return user_info

    # Add User to the database
    def insert_user_to_db(self):
        """
        Use user_info dic generated by user_info_to_dic()
        as data to insert into the db.
        """
        try:
            users_coll.insert_one(self.user_info_to_dic())
        except Exception as e:
            print(e)

    # method that can be used without instantiating the class,
    # but relevant to the class.
    @staticmethod
    def get_one_user_coll(username):
        """
        Get a user from the db with its username
        Return a user collection
        """
        try:
            user = users_coll.find_one({'username': username})
            return user
        except Exception as e:
            print(e)

    @staticmethod
    def update_user(new_info, user_id):
        """
        Takes a dictionary with the new value(s) to update 
        and the user _id as parameters.
        Update db
        """
        try:
            users_coll.update_one({'_id': ObjectId(user_id)},
                              {'$set': new_info})
        except Exception as e:
            print(e)

    @staticmethod
    def append_user_info(new_value, user_id):
        """
        Takes attribute and new info as param,
        Append new info and Update db
        """
        # unpack the tuple
        (get_attr, event_id) = new_value

        try:
            # get the user and corresponding attr/key and append the new value
            user = users_coll.find_one({"_id": ObjectId(user_id)})
            if user[get_attr] is not None:
                appended_info = user[get_attr].append(ObjectId(event_id))
                new_list = {get_attr: appended_info}
                users_coll.update_one({'_id': ObjectId(user_id)},
                                    {'$set': new_list})
            else:
                appended_info = [ObjectId(event_id)]
                new_list = {get_attr: appended_info}
                users_coll.update_one({'_id': ObjectId(user_id)},
                                    {'$set': new_list})

        except Exception as e:
            print(e)

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user from the db using the user_id
        """
        try:
            users_coll.delete_one({'_id': ObjectId(user_id)})
        except Exception as e:
            print(e)

    @staticmethod
    def check_if_username_exists(username):
        """
        Verify if the username already exists,
        return the corresponding user collection
        """
        try:
            existing_username = users_coll.find_one({'username': username})
            return existing_username
        except Exception as e:
            print(e)

    @staticmethod
    def check_if_email_exists(email):
        """
        Verify if the email already exists,
        return the corresponding user collection
        """
        try:
            existing_email = users_coll.find_one({'email': email})
            return existing_email
        except Exception as e:
            print(e)

    @staticmethod
    def convert_img_to_base64(profile_image):
        """
        Take an image path, read the image content and 
        convert it to Base64 in order to store it in the db.
        Remove the newly created file by the save() method of FileStorage.
        Return a new b64 srting.
        """

        with open(profile_image, "rb") as img_url_bytes:
            img_url_encoded = base64.b64encode(img_url_bytes.read()).decode('utf8')
            os.remove(profile_image)
            return img_url_encoded
