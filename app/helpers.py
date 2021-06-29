class User:

    """
    Class that Creates an instance of a user,
    Prepares the data for the database and
    Inserts the data in the users collection.
    """

    def __init__(self, first_name, last_name, username, email, password,
                profile_picture, event_liked, question_liked, answer_liked,
                contact_liked, tip_liked, event_created, question_created,
                answer_created, contact_created, tip_created):
                self.first_name = first_name
                self.last_name = last_name
                self.username = username
                self.email = email
                self.password = password
                self.profile_picture = profile_picture
                self.event_liked = event_liked
                self.question_liked = question_liked
                self.answer_liked = answer_liked
                self.contact_liked = contact_liked
                self.tip_liked = tip_liked
                self.event_created = event_created
                self.question_created = question_created
                self.answer_created = answer_created
                self.contact_created = contact_created
                self.tip_created = tip_created