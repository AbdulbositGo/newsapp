from flask import redirect, render_template, request, url_for 
from uuid import uuid4
import os

from models import News, Author, Category, db
from config import app, OS_UPLOAD_PATH


@app.route("/admin/news/")
def admin_news_view():
    if ("action" and "id") in request.args:
        try:
            _id = int(request.args.get("id"))
        except:
            return redirect(url_for(admin_news_view))

        news = News.query.filter_by(id=_id).first_or_404()
        action =request.args.get('action')
        if action == "make_active":
            news.is_published = True
        
        elif action == 'make_passive':
            news.is_published = False

        elif action == "delete":
            if news.photo:
                os.unlink(os.path.join("static","upload", "images", news.photo))
            db.session.delete(news)

        else:
            return redirect(url_for("admin_news_view"))
        
        db.session.commit()
        return redirect(url_for("admin_news_view"))

    all_news = News.query.all()
    return render_template("admin/admin-news.html", news=all_news)


@app.route("/admin/news/create", methods=["POST", "GET"])
def create_news_view():
    author = Author.query.all()
    category = Category.query.all()
    if request.method == "POST":
        news_title = request.form['title']
        news_content = request.form['content']
        news_author = request.form.get('author', None)
        news_category = request.form.get('category', None)
        news_published = bool(request.form.get('is_published', False))
        news_image = request.files.get('image', False)
        if news_image:
            photo_name = str(uuid4()) + "." + news_image.filename.split(".")[-1]
            news_image.save(os.path.join(OS_UPLOAD_PATH, photo_name))
            new_news = News(title=news_title, content=news_content, author_id=news_author, category_id=news_category, is_published=news_published, photo=photo_name)
        else:
            new_news = News(title=news_title, content=news_content, author_id=news_author, category_id=news_category, is_published=news_published, photo=None)
        db.session.add(new_news)
        db.session.commit()
        return redirect(url_for("admin_news_view"))

    return render_template("admin/create_news.html", categorys=category, authors=author)


@app.route("/admin/news/update<newsurl><newsid>", methods=["POST", "GET"])
def update_news_view(newsurl, newsid):
    news = News.query.filter_by(id=newsid, slug=newsurl).first_or_404()
    if "action" in request.args:
        action = request.args.get('action')
        if action == "delete_image":
            if news.photo:
                os.unlink(os.path.join("static","upload", "images", news.photo))
            news.photo = None
            db.session.commit() 
            return redirect(url_for("update_news_view", newsid=news.id, newsurl=news.slug))
    
    if request.method == "POST":
        news.title = request.form['uptitle']
        news.content = request.form['upcontent']
        news.author_id = request.form.get('upauthor', None)
        news.category_id = request.form.get('upcategory', None)
        news.is_published = bool(request.form.get('upis_published', False))
        upimage = request.files.get("upimage", None)

        if upimage:
            news_image = request.files.get('upimage')
            photo_name = str(uuid4( )) + "." + news_image.filename.split(".")[-1]
            news_image.save(os.path.join(OS_UPLOAD_PATH, photo_name))
            if news_image.filename.split(".")[-1] != "":
                news.photo = photo_name

        db.session.commit()
        return redirect(url_for("admin_news_view"))
        
    return render_template("admin/update-news.html", news=news)