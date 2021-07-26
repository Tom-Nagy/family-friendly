"""
Flash messages
"""

# Profile
class ProfileMsg:
    """
    class containing flash messages related to user info
    """

    username_exists = "Sorry this username is already taken, please choose a different one."

    email_exists = "The email provided already exist, please choose a different one."

    invalid_passwords = "Passwords must match, Please enter valid passwords."

    incorrect_password = "Incorrect password, try again."

    incorrect_details = "Incorrect details, enter the correct credentials."

    signed_in = "Well done and Welcome to the Family!"

    logged_in = "Welcome back to the Family!"

    logged_out = "You have been logged out."

    password_changed = "Your password has been changed."

    info_updated = "Your information have been updated."

    picture_updated = "The profile picture has been changed."

    profile_deleted = "Your profile has been deleted, sign up to access full website features."

# Events
class EventsMsg:
    """
    class containing flash messages related to event info
    """
    event_created = "Event successfully created !"
    event_deleted = "Event successfully deleted"
    event_joined = "You have joined the Event"
    didnt_work = "Sorry it did not work, try again later"