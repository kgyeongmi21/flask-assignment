from app import db


class User(db.Model):
    __table__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class Post(db.Model):
    __table__ = 'posts'
    postid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(4096))
    userid = db.Column(db.Integer)
