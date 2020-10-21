from flask import render_template, redirect, url_for, Blueprint

from app import db
from forms import WriteForm
from models import User, Post

main_blueprint = Blueprint('', __name__)


@main_blueprint.route('/')
def board_page():
    posts = Post.query.all()
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
            print(user)
            db.session.add(user)
            db.session.commit()

        post = Post(
            title=form.title.data,
            body=form.content.data,
            userid=user.userid
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.board_page'))
    return render_template("write.html", form=form)


@main_blueprint.route('/post/delete')
def delete_page():
    return render_template("post_delete.html")


@main_blueprint.route('/post/<postid>')
def post_page(postid):
    post = Post.query.filter_by(postid=postid)
    return render_template("post_list.html", post=post)


@main_blueprint.route('/user/<userid>')
def author_page():
    return render_template("author_list.html")


@main_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
