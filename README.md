# CommentApp
Simple [Firebase](https://firebase.google.com) + [Flask](http://flask.pocoo.org/) anonymous comment web app. Homework done @ IIC2173 PUC. Application deployed at Google Cloud Platform, using a VM Instance, on Ubuntu 18.04.

### Stack

**Why Flask?** The expected application is really simple: an anonymous comment application. The simplest design should have few routes: the comment form (`/`), a view of the created comments (`/comments`) and a route to create the comments (`/comments/new`).

**Why GCP?** It's free trial and complete status panel made easy to start the development. It's Cloud Shell allowed to try different comments and setup a custom environment really fast. Bad things? Most of the interesting solutions involve working with more GCP services, but I avoid using another machine. I end up using Firebase (I know it's related to Google anyway).

**Why Ubuntu 18.04?** It's the same version I use on Windows Subsystem for Linux (WSL), on Windows 10, so I'm familiarized with it.

**Why Firebase?** Fast, easy to setup and free.

### Solution

The application is simple. The routes were created with Flask, and the comments were stored using sqlite. Once the solution was deployed, there were problems while saving updates to the file used as database. So, instead of relying in a file (at least one living in the same server) I preferred to store the comments in a Firebase database, using its API through a simple wrapper, [Pyrebase](https://github.com/thisbejim/Pyrebase).

> To be honest, I tried different solutions:
>
> * Flask + sqlite, on Google App Engine: Didn't work because I was not able to update a file on production (also, wasn't sure if it was running on port 80)
> * Flask + Firebase, on Google App Engine: It worked! But it was weird to work without touching a server. Something was wrong.
> * **Flask + Firebase, on Google VM Instance**: After a lot of trouble trying to use the right port, it worked :sparkles:

### References

* [Explore-flask: Organizing your project — Explore Flask 1.0 documentation](https://explore-flask.readthedocs.io/en/latest/organizing.html): Used to decide which the pattern to organize files and folders of the application. Initial development was made following the "single module pattern", but the final application uses the "package pattern".
* [Medium: Build Simple Restful Api With Python and Flask Part 2](https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12): The first version of this homework used [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) and [sqlite](https://www.sqlite.org/index.html) to store comments, while running on Google App Engine, but it was not possible to setup, even from inside (used [Google Cloud: Debugging an Instance](https://cloud.google.com/appengine/docs/flexible/python/debugging-an-instance)). The final version uses Firebase to avoid working with files while storing data. Also, I have full control by using a VM (I didn't use it earlier because I forgot that using the 80 port was a requirement). **Disclaimer:** A portion of the code was taken from this article.
* [GitHub: uwi-info3180/flask-sqlite](https://github.com/uwi-info3180/flask-sqlite): From this repository was taken the idea of using [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/) to display a simple form to allow users to create a comment by just writing the body of it.