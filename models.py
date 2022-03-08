from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import app
from falchemy import slugify


db = SQLAlchemy(app)



class Author(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column("ismi", db.String(255))


class Category(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(255))


class News(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("sarlavha", db.String(255))
    content = db.Column("matni", db.Text)
    slug = db.Column("url_manzili", db.String())
    date_time = db.Column("sana", db.DateTime, default=datetime.now())
    views = db.Column("ko'rishlar", db.Integer, default=0)
    photo = db.Column("rasm", db.String(255))
    is_published = db.Column("chop etish", db.Boolean)
    author_id = db.Column("muallif_id", db.Integer, db.ForeignKey("author.id"))
    category_id = db.Column("kategoriya_id", db.Integer, db.ForeignKey("category.id"))


    def __init__(self, *args, **kwargs):
        if not "slug" in kwargs:
            kwargs["slug"] = slugify(kwargs["title"]) 
        super().__init__(*args, **kwargs)


class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    fullName = db.Column("To'liq ism", db.String(255))
    username = db.Column("Login", db.String(20))
    password = db.Column("Parol", db.String(25))


if __name__ == "__main__":
    db.create_all()