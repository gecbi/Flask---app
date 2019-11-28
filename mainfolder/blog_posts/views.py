#blog_post/views.py
from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from mainfolder import db
from mainfolder.models import BlogPost
from mainfolder.blog_posts import BlogPostForm

blog_post = Bluerint('blog_post', __name__)

# CREATE
@blog_post.route('/create', methods = ['GET', 'POST'])
@login_required
def create_post ():
    form = BlogPost()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        

# BLOG POST (VIEW)
# UPDATE
# DELETE
