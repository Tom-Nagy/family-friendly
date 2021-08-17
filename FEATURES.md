# FEATURES

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[Family Friendly :arrow_right:](https://family-friendly-app.herokuapp.com/)**.

## Table of Content

* [Existing Features](#Existing-Features)
* [Features to Implement in the Future](#Features-to-Implement-in-the-Future)

## Existing Features

### Common features

The navigation menu is fix and provide different links regarding if the user is Logged in or not.
The footer offers a link to contact the website owner, privacy policy and copyright.  
Form where user can change/update information and a cancel button to abort the action undertaken.

#### Always visible

* Logo linked to the home page on the top left.
* Events link on the top right of the screen.

#### If not Logged in

* Sign up and Login option will be provided on the top left of the screen.

#### If Logged in

* Logout option will replace login/sign up.
* Create link is provided on the top right of the screen.
* Profile link is provided on the top right of the screen.

### Home

The home page presents the Name of the website with and subtitle that explain the main goals of the website.  
Below, two buttons give the user the choice to navigate to Events and to Create.

#### About

The About section of the website is accessible from the home page and is presented as a button. This button will open a modal with the description of the website.

### Events

This page present the user with all the events available to attend in the future.  
It is presented as collapsible that toggle more information when clicked on.  
A sorting option is available for the user to be able to look for specific activities, ages etc.  
Buttons offer the possibility to see an event and then depending on user and event information to join, cancel, edit or leave an event.  
As well a participant count is shown to provide information about how busy and/or popular the event is.

### Create

This page gives the user the possibility to create an event of his own. To do so the user will have to create a profile by signing up.  
It provides a simple form to fill up and two buttons for either submitting or canceling the request.

### Sign up

Form to fill up in order to create a profile and be able to use all the website features.  
There is a link below the form linking to the login page. It is a common practice and provides better UX.

### Login

Page where user connect to their account/profile in order to access their profile and all the website features.

### Profile

Page where user can add and edit personal information.  
It gives the possibility to delete the profile. Upon deleting a message gives the user information about data stored and the steps to follow to retrieve or delete this data.  
There is a section that displays the event he or she is participating in. It provides option to cancel, edit or leave an event.  
A sorting button is provided in order to only show the event created by the user.  
A default profile picture is displayed representing the top flower of the website logo.  

3 links provide the user the possibility to update/change:

* Profile picture
* Profile information
* Password

### Update Profile

Prepopulated form where user can update their information:

* First name
* Last name
* Email
* Username

### Update Profile Picture

Form where user can upload an image they will use for their profile picture.  
Only ``.png`` file are accepted for profile picture.

### Change Password

[**:back:** *Table of Content*](#Table-of-Content)

## Features to Implement in the Future

### Support section

This page will provide three buttons corresponding to the sections of the page. When scrolling down or clicking on a button, they collapse to form a fix menu in order to help navigation on this page.

You can see below the wireframes concerning those features:

* [Support page](app/static/images/README-images/wireframes/support.pdf)
* [Useful contacts page](app/static/images/README-images/wireframes/useful-contacts.pdf)
* [Propose a contact page](app/static/images/README-images/wireframes/propose-contact.pdf)
* [Parenting tips page](app/static/images/README-images/wireframes/parenting-tips.pdf)
* [Propose a tip page](app/static/images/README-images/wireframes/propose-tip.pdf)
* [Forum access page](app/static/images/README-images/wireframes/forum-access.pdf)
* [Forum page](app/static/images/README-images/wireframes/forum.pdf)
* [Ask a question page](app/static/images/README-images/wireframes/ask-question.pdf)
* [Reply page](app/static/images/README-images/wireframes/reply.pdf)

#### Useful contacts

Section of support that provides information about contact useful for parents.  
It is presented as a carousel.  
There is as well the possibility to propose a contact and to delete or edit a contact depending on the user status regarding this contact.

#### Propose a contact

Form to fill up in order to propose a contact to add to the list.  
Offer the possibility to submit or cancel the request.

#### Parenting tips

Section of support that provides tips and advices on parenting.  
It is presented as a carousel.  
There is as well the possibility to propose a tip and to delete or edit a tip depending on the user status regarding this tip.

#### Propose a tip

Form to fill up in order to propose a tip to add to the list.  
Offer the possibility to submit or cancel the request.

#### Forum access

This page presents the rules of the forum platform.  
It presents a button to click in order to enter the forum.

### Forum

Platform where users can read post about parenting subject.  
It is presented as question and answer type of dialogue.  
A sorting menu provide help to display the relevant content.  
As well a search bar is provided in order to look for more specific content.

#### Ask a question

Form to fill up in order to ask a question on the forum.  
Offer the possibility to submit or cancel the request.

#### Reply

Form to fill up in order to reply to a question on the forum.  
Offer the possibility to submit or cancel the request.

[**:back:** *Table of Content*](#Table-of-Content)