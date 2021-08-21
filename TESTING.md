# TESTING

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[Family Friendly :arrow_right:](https://family-friendly-app.herokuapp.com/)**.

## Table of Content

* [Code Validation](#Code-Validation)
  * [W3C](#W3C)
  * [JSHint](#JSHint)
  * [PEP8](#PEP8)
  * [Regex](#Regex)
* [Lighthouse](#Lighthouse)
* [Cross Browsers Testing](#Cross-Browsers-Testing)
  * [Manual Testing](#Manual-Testing)
  * [Conclusions and Notations](#Conclusions-and-Notations)
* [User Stories Testing from UX section of the README.md](#User-Stories-Testing-from-UX-section-of-the-README.md)
  * [First Time User](#First-Time-User)
  * [Returning User](#Returning-User)
* [Further Testing](#Further-Testing)
* [Bugs](#Bugs)

## Code Validation

All code validation has been done using text input. This allows to check HTML without getting error with the Jenja templating language used with Flask.

### W3C

W3C Markup Validation Service and W3C CSS Validation Service have been used to check all the pages of the website for semantic and syntax errors.
The results are positive, and the code is valid.

* [W3C Markup Validation Service](https://validator.w3.org/)
  * home.html
    * ![W3C HTML Validation Result home.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-home.png)
  * events.html
    * ![W3C HTML Validation Result events.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-browse-events.png)
  * change-password.html
    * ![W3C HTML Validation Result change-password.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-change-password.png)
  * contact.html
    * ![W3C HTML Validation Result contact.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-contact.png)
  * create_event.html
    * ![W3C HTML Validation Result create-event.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-create-event.png)
  * delete_profile.html
    * ![W3C HTML Validation Result delete_profile.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-delete-profile.png)
  * 404.html
    * ![W3C HTML Validation Result 404.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-error-page.png)
  * login.html
    * ![W3C HTML Validation Result login.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-login.png)
  * privacy_policy.html
    * ![W3C HTML Validation Result privacy_policy.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-privacy-policy.png)
  * profile.html
    * ![W3C HTML Validation Result profile.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-profile.png)
  * see_event.html
    * ![W3C HTML Validation Result see_event.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-see-event.png)
  * signup.html
    * ![W3C HTML Validation Result signup.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-signup.png)
  * update_event.html
    * ![W3C HTML Validation Result update_event.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-update-event.png)
  * update_picture.html
    * ![W3C HTML Validation Result update_picture.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-update-picture.png)
  * update_profile.html
    * ![W3C HTML Validation Result update_profile.html](app/static/images/README-images/TESTING-images/code-validation/html-validator-update-profile.png)

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  * ![W3C CSS Validation Result](app/static/images/README-images/TESTING-images/code-validation/css-validator.png)

[**:back:** *Table of Content* ](#Table-of-Content)

### JSHint

[JSHint](https://jshint.com/) was used to validate the JavaScript code for semantic and syntax errors. No warnings or error were found.  
The results are positive, and the code is valid.

### PEP8

[PEP8 online](http://pep8online.com/) was used to validate the Python code for semantic and syntax errors. No warnings or error were found.  
The results are positive, and the code is valid.

Exception:  
one line of code is too long and correspond to the regex pattern variable for password validation.

### Regex

[Regex101](https://regex101.com/) to check implementation of regex pattern.

## Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) is a tool provided by Google Chrome DevTools and allows to identify the site performance, accessibility and user experience on Mobile and Desktop.  
All the pages from the website have been tested with Lighthouse.

* The scores given by Lighthouse for:

  * **SEO** (Search Engine Optimization) show **Crawling and Indexing** issues with invalid robots.txt file. I have done some research but found the subject out of scope and myself in the complete dark, running out of time I decided to leave it the way it is.

  * **Accessibility** show issues regarding contrast. Those apply to some material icons that are only esthetic element and provide no information to the user. ``aria-hidden="true"`` has been added to those elements

  * **Accessibility** show issue regarding form label. This is raised by the fact that Materializecss used javascript to change the ``select`` tag to an input that does not have a corresponding label. So error is shown even though the select tag has a corresponding label. As well the date and time input have a default label and therefor through an error.

  * **Best Practice** show issues regarding image size and more precisely the favicon size expectation against the size produced on the website. Even after changing to the expected size shown by the error, the issue still exist with different sizes. This is not a major issue and I decided to leave it that way at the moment.

* home.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-home.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-home.png)
* change_password.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-change-password.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-change-password.png)
* contact.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-contact.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-contact.png)
* create_event.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-create-event.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-create-event.png)
* delete_profile.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-delete-profile.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-delete-profile.png)
* error_page.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-error-page.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-error-page.png)
* events.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-events.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-events.png)
* login.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-login.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-login.png)
* privacy_policy.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-privacy-policy.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-privacy-policy.png)
* profile.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-profile.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-profile.png)
* see_event.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-see-event.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-see-event.png)
* signup.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-signup.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-signup.png)
* update_event.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-update-event.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-update-event.png)
* update_picture.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-update-picture.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-update-picture.png)
* update_profile.html
  * ![Mobile](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-mobile-update-profile.png)
  * ![Desktop](app/static/images/README-images/TESTING-images/lighthouse/lighthouse-desktop-update-profile.png)

[**:back:** *Table of Content* ](#Table-of-Content)

## Cross Browsers Testing

The website was tested on several browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari and Opera) and shows good functionality across them all.  

### Manual Testing

Manual testing was executed on **all browsers** as shown in the following section.

The responsiveness of the website for different viewport sizes was tested by dragging the window up, down, left and right.  
The following tests have been executed several times at different viewport breakpoints.

* Buttons on hover :heavy_check_mark:
* Buttons on focus :heavy_check_mark:
* Buttons on active :heavy_check_mark:
* Clicking Buttons and expecting behavior happens :heavy_check_mark:
* Link on hover :heavy_check_mark:
* Link on focus :heavy_check_mark:
* Link on active :heavy_check_mark:
* Clicking Link and expecting behavior happens :heavy_check_mark:
* Validation of inputs :heavy_check_mark:
* Submitting Forms :heavy_check_mark:
* Modal Triggers :heavy_check_mark:
* Like and unlike event :heavy_check_mark:
* Create/Update(Edit)/Delete events :heavy_check_mark:
* Join/Leave events :heavy_check_mark:
* Create/Update(Edit)/Delete profile :heavy_check_mark:
* Change Password :heavy_check_mark:
* Image upload size when updating image profile :heavy_check_mark:
* Login and Log out :heavy_check_mark:
* Contact :heavy_check_mark:
* Search event with input :heavy_check_mark:
* Search event with select :heavy_check_mark:

### Conclusions and Notations

All the features and functionality works very well across browser except for some features on safary and iOS.

Noted issues on iPhones and iOS:

* The display of the date and time picker is not rendering. The input is working when clicking on it, but the labels don't show. Instead, we see and input line.

Noted general issue:

* The select form element from materialize is not very easy to adjust in the front end and could cause a negative effect on the UX.
* Because of bad time and date picker behavior with materialize library, I have opted for the default browser one which works but is not the best UI.
* It is possible to search events by date, but It would be a great addition to add some validation on the date of the event in order to delete it if the date is passed.
* On the same last note, the events appear in order of creation and not by the closest from "today".

All those points are not major bugs to fix and will be implemented in the near future with the support section of the website.

[**:back:** *Table of Content* ](#Table-of-Content)

## User Stories Testing from UX section of the README.md

### First time users

As a first time user:

1. I want the application to be **easy to navigate** and **appealing**. :thumbsup:
    * The website is straight forward with little manipulation to reach the main sections of it. As well, it uses the Materialize library that is UX focus and provide great UI.

2. I want to find information in an obvious manner without having to look for it. :thumbsup:
    * The website is very specific and therefor very clear to navigate through its content.

3. I want to **find events** and identify instantly:
    1. The type of **activity**. :thumbsup:
    2. The appropriate **age** to participate. :thumbsup:
    3. The **location**. :thumbsup:
    4. The **date and time**. :thumbsup:
    * Events are presented in collapsible that show The activity, date, number of participant and like as first information. When clicking on the event, it shows the location, the time, the description and the age range.

    * ![Event](app/static/images/README-images/TESTING-images/manual-testing/event-info.png)

4. I want to **sign up** and create a profile. :thumbsup:
    * A sign up link is always presented in the navigation bar if the user is not logged in.
    * When signing up, the user is directed to his profile page where he can change his information and add a picture.

5. I want to **log in**.
    * A log in link is always presented in the navigation bar if the user is not logged in.
    * ![Login/Signup](app/static/images/README-images/TESTING-images/manual-testing/login-signup.png)

6. I want to **log out**.
    * A log out link is always presented in the navigation bar if the user is logged in.
    * ![Logout](app/static/images/README-images/TESTING-images/manual-testing/logout.png)

7. I want to be able to **join** an event.
    * When browsing events, the user has the possibility to click on ``see`` in order to see the event. This offer then the possibility to join an event.
    * ![Join Event](app/static/images/README-images/TESTING-images/manual-testing/join-event.png)

8. I want to be provided with **easy instructions** on how to create an event.
    * The forms are very easy to fill up and straight forward with helper text when needed.
    * ![Create Event](app/static/images/README-images/TESTING-images/manual-testing/create-event.png)

9. I want to be able to **create** an event.
    * The User once logged in or sign up has the option of creating an event.
    * ![Create Event link](app/static/images/README-images/TESTING-images/manual-testing/create-event-link.png)

10. I want to have access to the **support** page where I can find:
    1. Useful **contacts**.
    2. Parenting **advices**.
    3. A space where I can **share ideas** and/or **ask questions** and advices.

    * The support section of the website will be launched in the next release in the near future.

### Returning users

As a returning user:

1. I want to be able to **cancel** my participation in an event.
    * When joined, and event can be left with the ``leave`` button.
    * ![Leave Event](app/static/images/README-images/TESTING-images/manual-testing/leave-event.png)

2. I want to be able to **cancel** an event I created.
    * When created, An event can be canceled.
    * ![Cancel Event](app/static/images/README-images/TESTING-images/manual-testing/cancel-event.png)

3. I want to be able to **modify** an event I created.
    * As well as leaving and event, the option of updating the event is given via the ``Update`` button.

4. I want to be able to **modify** my profile.
    * When a profile is Created, the user can Update his profile and delete his profile.

All the following user story will be answered in the next release of the website in the near future.

5. I want to be **notified** when there is a change on an event I am participating in.
6. I want to be **notified** when people join or cancel an event I Created.
7. I want to **post** a question or advice on the support page.
8. I want to **edit or delete** a question or advice I created on the support page.
9. I want to **participate** in topic on the support page.
10. I want to **propose** a useful contact.

[**:back:** *Table of Content* ](#Table-of-Content)

## Further Testing

* The website has been tested by fellow students, slack community, friends and family.
* All the issues raised have been addressed.

* An issue has appeared on the console when loading the page:

![Warning](app/static/images/README-images/TESTING-images/manual-testing/dev-tool-error.png)

[**:back:** *Table of Content* ](#Table-of-Content)