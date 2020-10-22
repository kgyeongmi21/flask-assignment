from flask import render_template, redirect, url_for, Blueprint, request, session

from app import db
from forms import WriteForm
from models import User, Post

main_blueprint = Blueprint('', __name__)


@main_blueprint.route('/')
def board_page():
    posts = Post.query.filter_by(userid=session.get('userid')).all()
    for post in posts:
        post.user = User.query.filter_by(userid=post.userid).first()
    return render_template("list.html", posts=posts)


@main_blueprint.route('/post/write', methods=['GET', 'POST'])
def writing_page():
    form = WriteForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.author.data).first()
        if user is None:
            user = User(
                name=form.author.data
            )
            db.session.add(user)
            db.session.commit()

        post = Post(
            title=form.title.data,
            body=form.content.data,
            userid=user.userid
        )
        db.session.add(post)
        db.session.commit()
        session['username'] = user.name
        session['userid'] = user.userid
        return redirect(url_for('.board_page'))
    return render_template("write.html", form=form)


@main_blueprint.route('/post/delete', methods=['POST'])
def delete_page():
    Post.query.filter_by(title=request.form['title']).delete()
    db.session.commit()
    return redirect(url_for('.board_page'))


@main_blueprint.route('/post/<postid>')
def post_page(postid):
    post = Post.query.filter_by(postid=postid).first()
    post.user = User.query.filter_by(userid=post.userid).first()
    form = WriteForm()
    form.title.data = post.title
    form.title.render_kw = {'readonly': True}
    form.author.data = post.user.name
    form.author.render_kw = {'readonly': True}
    form.content.data = post.body
    form.content.render_kw = {'readonly': True}
    form.submit.render_kw = {'style': 'display: none'}
    return render_template("detail.html", form=form)


@main_blueprint.route('/user/<userid>')
def author_page(userid):
    posts = Post.query.filter_by(userid=userid).all()
    user = User.query.filter_by(userid=userid).first()
    return render_template("author_list.html", posts=posts, user=user)


@main_blueprint.route('/user/delete', methods=['POST'])
def author_delete():
    posts = Post.query.filter_by(userid=request.form['userid']).delete()
    user = User.query.filter_by(userid=request.form['userid']).delete()
    db.session.commit()
    return redirect(url_for('.board_page'))


def page_not_found(e):
    return render_template("404.html"), 404
