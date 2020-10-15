# Django Feedback Form

This project is builts for creating and viewing feedbacks for a speific registered user.

My project contains Custom CSS with some extent of Bootstrap4 on the FrontEnd.

Crispy Forms are used for handling validation front-end
A little tat of Javascript is also there to give sort of a visual feedback to the User, fillling the form

Features
--------

* __For Rating Given >= 7__

![Positive](/img/green.png)


* __For 3>Rate< 7__

![Neutral](/img/Blue.png)


* __For Rating Given <= 3__

![Negative](/img/red.png)

* __For every question there is average score given by all the users and a total average score.__

![Feedback Response View](/img/FeedView.png)

Requirements
------------

1. [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

Installation
------------

All things are already been configured into the project. You'd just have to `git clone https://github.com/sudolmin/django_feedback_form.git` 

`cd django_feedback_form` into the directory and Run `python3 manange.py runserver`

