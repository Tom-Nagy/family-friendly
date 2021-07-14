"""
Views related to the creation of events
"""

from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for, Blueprint, current_app)
# from app.flashes.flash_messages import *

create = Blueprint("create", __name__)

@create.route("/create_event")
def create_event():
    return render_template('create_event.html')
