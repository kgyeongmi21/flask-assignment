import os

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Xylq5waRm51AeOky0pnSeopVNdSlKRXTrgcRzTBMm8gAGUG22miVMXAUGlZF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

@app.route('/')
def board_page():
    return render_template("list.html")


@app.route('/post/write')
def writing_page():
    return render_template("write.html")


@app.route('/post/delete')
def delete_page():
    return render_template("post_delete.html")


@app.route('/post/<postid>')
def post_page():
    return render_template("post_list.html")


@app.route('/user/<userid>')
def author_page():
    return render_template("author_list.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run()
