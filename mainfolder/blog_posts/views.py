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

        db.session.add(blog_post)
        db.session.commit()
        flash ('Blog Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form =form)

# BLOG POST (VIEW)
@blog_post.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post= BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=blog_post.title,
    date=blog_post.date, post=blog_post)

# UPDATE
@blog_post.route('/<int:blog_post_id/update', methods= ['GET','POST'])
@login_required
def update(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        aborth(403)

    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data

        flash('Blog Post Updated')
        return redirect(url_for('blog_post.blog_post'), blog_post_id = blog_post_id)

    elif request.method = 'GET':

        form.text.data = blog_post.text
        form.title.data = blog_post.title

    return render_template('create_post.html', title ='Updating', form =form)

# DELETE
@blog_post.route('/<int:blog_post_id/delete', methods = ['GET', 'POST'])
@login_required

def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        aborth(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')

    return redirect(url_for('core.index'))
    
