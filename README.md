# **Family Friendly**

![Mockup](assets/images/README-images/mockups/ami-responsive-website.png)

Check out the other mockups:

* [Home page](assets/images/README-images/mockups/ami-responsive-home.png)

#### Visit the live Website : **[Family Friendly :arrow_right:](WEBSITE LINK)**.

**Family Friendly** is a community based application where families can get together and have fun. This project promotes **togetherness**, **fun** and **community** through **activities**.  
It is difficult sometimes as new or experience parents to find the motivation to go out and do something with the hectic parenting life. You would have to organize something or think about going somewhere on top of preparing what you need to bring with you for your little one and for yourself. So you would consider doing nothing, stay put and deal with the craziness happening at home. A lot of different factors could amplify the sentiment.  
This can lead to inactivity, confinement and mental distress which only feed the vicious cycle.

In order to help parents and/or caretaker, I propose **Family Friendly**.  
This platform will propose features including a list of **events** coming up, the possibility to **create** and **join** event and access to **support** that provide useful *contacts* and *information*. As well a **forum** that allow users to share tips and help each other in a format of *Question* and *Answer*.

## Table of Content

* [Project](#Project)
  * [Project Goals](#Project-Goals)
  * [Developer and Business Goals](#Developer-and-Business-Goals)
  * [User Goals](#User-Goals)
* [UX](#UX)
  * [Audience Definition](#Audience-Definition)
  * [User Stories](#User-Stories)
  * [Design Choices](#Design-Choices)
  * [Wireframes](#Wireframes)
  * [Different Design](#Different-Design)
* [Features](#Features) [:fast_forward: FEATURES.md](FEATURES.md)
* [Flowchart](#Flowchart)
* [Code Organisation](#Code-Organisation)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing) [:fast_forward: TESTING.md](TESTING.md)
* [Deployment](#Deployment) [:fast_forward: DEPLOYMENT.md](DEPLOYMENT.md)
  * [Live Deployment](#Live-Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Implementing API](#Implementing-API)
* [Bugs](#Bugs)
  * [Solved](#Solved)
  * [Unsolved](#Unsolved)
* [Credits](#Credits)
  * [Content](#Content)
  * [Media](#Media)
  * [Acknowledgements](#Aknowledgements)

## Project

### Project Goals

This project is offering an application with a welcoming and fun environment to enable and empower users to go out, join activities and events. Encourage users to meet with the community, have fun and share good memories. It promotes healthy lifestyle and mental health.

### Developer and Business Goals

* Develop an interactive website with a server connection using HTML, CSS, JavaScript and Python.
* Provide a user-friendly application.
* Contribute to the community.
* Help parents.
* Promote Wellness and health through activities.
* Help personal and family growth.

### User Goals

* Easy to use application.
* Getting clear information.
* Quick access to Events.
* Practical way to participate and be part of the community.

[**:back:** *Table of Content*](#Table-of-Content)

## UX

### Audience definition

1. The primary targeted audience is Families and more precisely **Parents**.
2. The secondary targeted audience is **Children**.

#### The primary audience for this application is looking for:

* Getting together.
* Going out and/or outside.
* Having fun as a family.
* Sharing parental tips/advise.
* Supporting each other.
* Socialization of the children.
* Participating in a healthy community.

#### The secondary audience for this application is looking for:

* Having fun.
* Discovering.
* Meeting and Making friends.

#### This application is the best way to answer their needs because:

* Activities are created and proposed by users, for them and the community.
* It provides the possibility to Create and Join Events.
* Events are accessible in a click.
* You can identify immediately if there is a suitable Event for you and your family.
* You can Create and Join Events on the go.
* It offers parenting tips and a space where parents can browse content relevant to them.
* It is a User Centric Design approach:
  * It is a simple application to use.
  * It is very specific and get to the point.
  * The information are displayed in a fashion that is not overwhelming and easy to learn.

### User stories

#### First time users

As a first time user:

1. I want the application to be **easy to navigate** and **appealing**.
2. I want to find information in an obvious manner without having to look for it.
3. I want to **find events** and identify instantly:
    * The type of **activity**.
    * The appropriate **age** to participate.
    * The **location**.
    * The **date and time**.
4. I want to **sign up** and create a profile.
5. I want to **log in**.
6. I want to **log out**.
7. I want to be able to **join** an event.
8. I want to be provided with **easy instructions** on how to create an event.
9. I want to be able to **create** an event.
10. I want to have access to the **support** page where I can find:
    * Useful **contacts**.
    * Parenting **advices**.
    * A space where I can **share ideas** and/or **ask questions** and advices.

#### Returning users

As a returning user:

1. I want to be able to **cancel** my participation in an event.
2. I want to be able to **cancel** an event I created.
3. I want to be able to **modify** an event I created.
4. I want to be able to **modify** my profile.
5. I want to be **notified** when there is a change on an event I am participating in.
6. I want to be **notified** when people join or cancel an event I Created.
7. I want to **post** a question or advice on the support page.
8. I want to **edit or delete** a question or advice I created on the support page.
9. I want to **participate** in topic on the support page.
10. I want to **propose** a useful contact.

[**:back:** *Table of Content*](#Table-of-Content)

### Design Choices

#### Fonts

Considering the targeted audience, the sans serif type of font is the more appropriate because it is most often associated with simplicity and straightforwardness.  
I will be using:

* *Pacifico* for the name of the website (Family Friendly) only. It is a handwriting type of font which is very friendly and welcoming with its roundness and has something fun to it that relates to the website.

* *Lato* and *Nunito* are used for the rest of the website. They both are sans serif fonts, and they work very well together. They are comforting, simple and easy to ready.

*Sans serif* will be use as a fall back if the fonts do not load. It is common as the main typographies are sans serif type.

#### Icons

* Some Font Awesome icons will be part of the website for better UX.
* The [logo](app/static/images/logo/logo.png) and [favicon](app/static/images/favicon/favicon.ico) are the same image and use the color scheme of the website.

![logo](app/static/images/logo/logo.png)

#### Colors

![Color palette](app/static/images/README-images/design/color.png)

The colours chosen for the website are simple and joyful. They are based on the psychology behind colours ([colour affects](http://www.colour-affects.co.uk/psychological-properties-of-colours), [London Image Institute](https://londonimageinstitute.com/how-to-empower-yourself-with-color-psychology/)). I used Adobe Color to create the colour scheme.

* Yellow #E9F900 for Friendliness and Warmth.
* Blue #0845FF for Confidence, Sincerity and Integrity.
* Red #FF091E for cancelling and deleting functionality.
* Orange #FF8401 for Creativity and Innovation.
* Green #24C212 for Life, Growth and Nature.
* The background will be off White #FAFAFA for simplicity and cleanliness.
* Footer will be Grey #999999 for a nice contrast.

[Adobe Color](https://color.adobe.com/create/color-accessibility) was used to build the color compatibility and accessibility. The color scheme and swatches are said color-blind safe.

![Color accessibility](app/static/images/README-images/design/color-accessibility.png)

#### Images

The images will be the one uploaded by users for their profile, or images shared on the support channel.

#### Styling/Feeling

The feel of the website is welcoming and simple to provide a quick access and learning process.  
It makes users comfortable and make them want to try!

#### Audio/Video

No audio or video will be integrated at the moment.

[**:back:** *Table of Content*](#Table-of-Content)

### Wireframes

![Site map](app/static/images/README-images/wireframes/site-map.png)

* [Home page](app/static/images/README-images/wireframes/home.pdf)
* [About page](app/static/images/README-images/wireframes/about.pdf)
* [Contact page](app/static/images/README-images/wireframes/contact.pdf)
* [Events page](app/static/images/README-images/wireframes/events.pdf)
* [Create page](app/static/images/README-images/wireframes/create.pdf)
* [Support page](app/static/images/README-images/wireframes/support.pdf)
* [Useful contacts page](app/static/images/README-images/wireframes/useful-contacts.pdf)
* [Propose a contact page](app/static/images/README-images/wireframes/propose-contact.pdf)
* [Parenting tips page](app/static/images/README-images/wireframes/parenting-tips.pdf)
* [Propose a tip page](app/static/images/README-images/wireframes/propose-tip.pdf)
* [Forum access page](app/static/images/README-images/wireframes/forum-access.pdf)
* [Forum page](app/static/images/README-images/wireframes/forum.pdf)
* [Ask a question page](app/static/images/README-images/wireframes/ask-question.pdf)
* [Reply page](app/static/images/README-images/wireframes/reply.pdf)
* [Sign up page](app/static/images/README-images/wireframes/signup.pdf)
* [Login page](app/static/images/README-images/wireframes/login.pdf)
* [Profile page](app/static/images/README-images/wireframes/profile.pdf)
* [404 page](app/static/images/README-images/wireframes/error.pdf)

For the full version:

* [Family Friendly website](app/static/images/README-images/wireframes/home.pdf)

[**:back:** *Table of Content*](#Table-of-Content)

### Different design

[**:back:** *Table of Content*](#Table-of-Content)

## Features

To build this project, I use Flask framework with the Jinja templating language. For consistency across the website some features will be repeated and functionality will be kept as simple and direct as possible.

Features are published in a separate file, please see [FEATURES.md](FEATURES.md) for full details.

## Flowchart

![Website flowchart](app/static/images/README-images/design/flowchart.jpg)
[Website flowchart pdf](app/static/images/README-images/design/flowchart.pdf)

[**:back:** *Table of Content*](#Table-of-Content)

## Code Organisation

The project uses Flask and I have implemented Application Factory and Blueprint allowing separation of concern and clearer code.

The code structure includes ``app.py`` file that initialise the App and a folder called ``app`` that host all the development code as well as the implementation of Blueprint in ``__init__.py`` and the App configuration in ``config.py``.

The use of Flask framework implies the creation of a ``static`` and templates ``folder``. The static folder host the ``*.js``, ``*.css``, ``*.json`` files and all images.

I have Created:

* A ``classes`` folder that will host the python files related to the classes used for the project.
* A ``validators`` folder that host the validation functions for the project.
* A ``flashes`` folder that host all the flash messages.

## Technologies Used

### Programming Languages

This project uses HTML, CSS and JavaScript.

### Frameworks, Libraries and Programs

* [Balsamiq](https://balsamiq.com/wireframes/)  
For creating wireframes.

* [miro whiteboard](https://miro.com/)  
For producing the flowchart.

* [Google Fonts](https://fonts.google.com/)  
<!-- For importing fonts (**Fredoka One**, **Handlee** and **Andika New Basic**) into the style.css file. -->

* [Font Awesome](https://fontawesome.com/icons?d=gallery)  
For using icons throughout the website.

* [favicon.io](https://favicon.io/favicon-converter/)  
For generating the favicon.

* [TinyPNG](https://tinypng.com/) or [Squoosh](https://squoosh.app/)  
For resizing all the images.

* [BeFunky](https://www.befunky.com/create/)
For cropping some images.

* [Adobe Color](https://color.adobe.com/create/image)  
For extracting the color scheme used on the website.

* [Am I Responsive?](http://ami.responsivedesign.is/?url=http://ami.responsivedesign.is/#)  
For providing screenshots of the responsiveness of the website across several devices.

* [techsini](http://techsini.com/multi-mockup/index.php)  
For Multi Device Website Mockup Generator.

* [Autoprefixer CSS online](https://autoprefixer.github.io/)  
For adding prefixer in style.css for cross browser compatibility.

<!-- * [EmailJS](https://www.emailjs.com/)  
For email service implementation using API and without server. -->

* [Git](https://git-scm.com/)  
For Version control.

* [GitPod](https://www.gitpod.io/)  
For Integrated Development Environment.

* [GitHub](https://github.com/)  
For hosting the repository.

* [Heroku](https://www.heroku.com/home)  
For deploying the website live.

* [MongoDB](https://www.mongodb.com/)  
For hosting the database.

[**:back:** *Table of Content*](#Table-of-Content)

## Bugs

Issue:  
I got the following message error: ``runtimeerror-working-outside-of-request-context``.
Solve:  
I saved ``request.form.get`` in a var named ``form_field`` in order to help me with coding and repetition, but a ``request`` in Flask is an instance of the Request object and handle one request at the time and therefore cannot be stored in a var.

Issue:  
When updating the profile info, the rendering of the info on the profile page don't update and after login out, It was not possible to log back in. I was getting the flash message ``incorrect_details``, but details were right.
Solve:  
The problem was because I used the User class to update the info, It hashed the password again, which I believe created a double hashed password and when checking the password validation It could not find a match.  
I changed the approach and did not convert the new info into an instance of User, but use a static method of the class taking as parameter the dictionary of the new info.

Issue:  
When Updating the profile info, the updated profile info don't render on the profile template when updating the username. This must be because I rely on the username when rendering the profile page.
Solve:  
Update the session cookie (``session["user"]``) after updating the database and before rendering the profile template with the new ``sesion["user"]``.

## Credits

**All the written subject's content provided on the website is the result of my research and are my own production.**  
Some resources used are but not limited to:

* [lelivrescolaire.fr](https://www.lelivrescolaire.fr/matiere/sciences-de-la-vie-et-de-la-terre)
* [Owlcation](https://owlcation.com/)
* [Kiddle](https://www.kiddle.co/)
* [NATIONAL GEOGRAPHIC](https://www.nationalgeographic.org/)
* [NATIONAL GEOGRAPHIC KIDS](https://www.natgeokids.com/ie/)
* [MONGABAY](https://rainforests.mongabay.com/)
* [Britannica](https://www.britannica.com/)
* [National Oceanic and Atmospheric Administration: NOOA](https://www.noaa.gov/)
* [USGS](https://www.usgs.gov/)
* [LIVESCIENCE](https://www.livescience.com/)
* [Wikipedia](https://www.wikipedia.org/)

### Content

[W3schools](https://www.w3schools.com/)  

[W3docs](https://www.w3docs.com/)

[stack overflow](https://stackoverflow.com/)

[GeeksforGeeks](https://www.geeksforgeeks.org/)

[Miguel Grinberg](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
### Media

#### External links

[ScienceNewsforStudents](https://www.sciencenewsforstudents.org/article/top-10-tips-study-smarter-not-longer-study-skills)  
[FocusMe](https://focusme.com/blog/8-tips-to-study-better/)  
[Pinterest 10 Study Tips by Diamond](https://www.pinterest.ie/pin/184225440993206363/)  
[Wikipedia 404 error definition](https://en.wikipedia.org/wiki/HTTP_404)

#### Icons

[Alexandr Martinov on Iconfinder](https://www.iconfinder.com/search/?q=book&price=free)  
For the menu icon that was slightly adjusted to the website needs using [Iconfinder Editor](https://www.iconfinder.com/editor/).

* Icon made by Freepik from [www.flaticon.com](www.flaticon.com):
  * [Volcano](https://www.flaticon.com/free-icon/volcano_2206644?term=volcano&page=1&position=3&page=1&position=3&related_id=2206644&origin=search)
  * [Jungle](https://www.flaticon.com/free-icon/volcano_2206644?term=volcano&page=1&position=3&page=1&position=3&related_id=2206644&origin=search)
  * [Ocean](https://www.flaticon.com/free-icon/ocean_3254422?term=ocean&page=1&position=8&page=1&position=8&related_id=3254422&origin=search)
  * [Earth](https://www.flaticon.com/free-icon/earth-globe_616616?term=earth&page=1&position=12&page=1&position=12&related_id=616616&origin=search)

#### Images

<!-- * For the Volcano content:  
  * [Infographic vector created by brgfx - www.freepik.com<](https://www.freepik.com/vectors/infographic)  
  Images from [Adobe Stock](https://stock.adobe.com/ie/):  
  * [volcano and earthquake infographic vector by gritsalak](https://stock.adobe.com/ie/images/volcano-and-earthquake-infographic-vector/211375558?prev_url=detail)  
  * [volcano type. shield, dome, composite, and caldera by designua](https://stock.adobe.com/ie/images/volcano-type-shield-dome-composite-and-caldera/319892493?prev_url=detail)  
  * [Part of a volcano by blueringmedia](https://stock.adobe.com/ie/images/part-of-a-volcano/377249194?prev_url=detail)

* For the Ocean content:  
  * [Oceans map by our homework help](https://ourhomeworkhelp.wordpress.com/2016/07/11/map-of-continents-oceans/)  
  * [Image by brgfx from [freepik](https://www.freepik.com)](https://www.freepik.com/free-vector/tidal-movements-earth_1466597.htm#page=1&query=ocean%20tides&position=49)  
  * [Image by U.S. Geological Survey, Department of the Interior/USGS Howard Perlman, USGS and John Evans, USGS. from Kiddle](https://kids.kiddle.co/Image:Water_cycle.png)  
  * [Image by U.S. Geological Survey, Department of the Interior/USGS Igor Shiklamonov, 1993, "Water in Crisis: A Guide to the World's Freshwater Resources"](https://www.usgs.gov/media/images/distribution-water-and-above-earth)  

* For the Jungle content:
  Images from [Adobe Stock](https://stock.adobe.com/ie/):  
  * [Rainforest layers educational banner or poster. Jungle vertical structure educational scheme. Emergent, canopy, understory and floor levels. Flat vector illustration by Rudzhan](https://stock.adobe.com/ie/images/rainforest-layers-educational-banner-or-poster-jungle-vertical-structure-educational-scheme-emergent-canopy-understory-and-floor-levels-flat-vector-illustration/408770051?prev_url=detail&asset_id=408770051)  
  * [Aerial view of deforestation. Rainforest being removed to make way for palm oil and rubber plantations by whitcomberd](https://stock.adobe.com/ie/images/aerial-view-of-deforestation-rainforest-being-removed-to-make-way-for-palm-oil-and-rubber-plantations/240813889?prev_url=detail&asset_id=240813889)

* For the Labyrinth path images depending on the subject selected:
Images from [Adobe Stock](https://stock.adobe.com/ie/):
  * Volcano: [heat red cracked ground texture after eruption volcano by releon8211](https://stock.adobe.com/ie/images/heat-red-cracked-ground-texture-after-eruption-volcano/110818846?prev_url=detail), 
  * Jungle: [Yellow brick wall seamless texture for jungle theme vector by Pallavi](https://stock.adobe.com/ie/images/yellow-brick-wall-seamless-texture-for-jungle-theme-vector/271949380?prev_url=detail),
  * Ocean: [blue water wave texture background by Naoki Kim](https://stock.adobe.com/ie/images/blue-water-wave-texture-background/154153098?prev_url=detail),
  * Earth: [Top view of a young green forest in spring or summer by artjazz](https://stock.adobe.com/ie/images/top-view-of-a-young-green-forest-in-spring-or-summer/207714693?prev_url=detail)

* For the exit sign in the labyrinth :
[Arrow vector created by freepik - www.freepik.com](https://www.freepik.com/vectors/arrow)

### Aknowledgements :

Special thanks to all Code Institute's team (“Teacher”, Lecturers and Tutors) that are making me more knowledgeable and are making this happen.

Huge thank you to the [Slack](code-institute-room.slack.com) community, all the members and all the leads and tutors for their help and support.

I am hugely grateful to my mentor Chris Quinn for guiding me through this project.
 -->
[**:back:** *Table of Content*](#Table-of-Content)