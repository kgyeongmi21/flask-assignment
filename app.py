import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config['SECRET_KEY'] = 'Xylq5waRm51AeOky0pnSeopVNdSlKRXTrgcRzTBMm8gAGUG22miVMXAUGlZF'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from view import main_blueprint, page_not_found
    app.register_blueprint(main_blueprint)
    app.register_error_handler(404, page_not_found)
    db.init_app(app)
    db.create_all(app=app)
    return app


if __name__ == '__main__':
    create_app().run()
