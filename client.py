import os
from flask import redirect, render_template, request
from sqlalchemy import true
from uuid import uuid4

from config import OS_UPLOAD_PATH, app
from falchemy import highlight_word

from models import News, Category, Author, Users, db


@app.route("/")
def home_view():
    term = request.args.get("term", None)
    category_id = request.args.get("category", False)
    if term:
        temp = []
        all_news = News.query.filter(News.title.contains(term) | News.content.contains(term)).all()
        for single_news in all_news:
            single_news.title = highlight_word(single_news.title, term)
            single_news.content = highlight_word(single_news.content, term)
            temp.append(single_news)
        all_news = temp

    elif category_id:
        all_news = News.query.filter_by(category_id=category_id).all()
    else:
        all_news = News.query.all()


    return render_template("client/home.html", news=all_news)


@app.route("/single-news/<newsurl><newsid>")
def single_news_view(newsurl, newsid):
    single_news = News.query.filter_by(id=newsid, slug=newsurl).first_or_404()
    single_news.views += 1
    db.session.commit()
    return render_template("client/single-news.html", single_news=single_news)


