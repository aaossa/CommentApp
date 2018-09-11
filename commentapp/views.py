from datetime import datetime

from json import dumps
from flask import flash, jsonify, redirect, render_template, request, url_for

from .app import app
from .forms import CommentForm
from .models import db


@app.route("/")
def index():
    """Display a form to create a comment."""
    comment_form = CommentForm()
    return render_template(
        'index.html',
        form=comment_form,
    )


@app.route("/comment/new", methods=["POST"])
def create_comment():
    """Create a new comment and store it in the database."""
    comment_form = CommentForm()
    # Validate form
    if not comment_form.validate_on_submit():
        return redirect(url_for('index'))
    # Create comment object
    new_comment = {
        "body": request.form['body'],
        # ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "created_at": str(datetime.now()),
    }
    # Save new_comment in db
    db.child("comments").push(new_comment)
    return redirect(url_for('show_comments'))


@app.route("/comments", methods=["GET"])
def show_comments():
    """Show existing comments."""
    all_comments = db.child("comments").get().val()
    return jsonify(all_comments)
