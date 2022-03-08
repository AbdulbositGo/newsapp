import re
from tabnanny import check
from time import sleep
from flask import redirect, render_template, request, session, flash, url_for
import bcrypt

from config import app
from models import Users, db

@app.route("/admin/users/login/", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        username = request.form.get("login_user_name", None)
        password = request.form.get("login_password", None)
        if (not username) or (not password):
            flash("User name yoki parol kiritilmadi")
        
        else:
            user = Users.query.filter_by(username=username.strip()).first()
            print(user.password)
            
            if user and (bcrypt.checkpw(password.encode(), user.password)):
                print(user.username)
                flash("tizimga mvaffaqiyatli kirdingiz")
                return redirect(url_for("admin_news_view"))
            else:
                flash("Login yoki parol xato")

    return render_template("admin/log-in.html")




@app.route("/admin/users/register", methods=["GET", "POST"])
def register_view():
    if request.method == "POST":
        fullname = request.form.get("register_fuul_name", None)
        username = request.form.get("register_user_name", None)
        password1 = request.form.get("register_password", None)
        password2 = request.form.get("register__password", None)

        if not fullname:
            flash("To'liq ism kiritilmadi")
        elif not username:
            flash("User name kiritilmadi")
        elif not password1:
            flash("Parol kiritilmadi")
        elif not password2:
            flash("Ikkinchi parol kiritilmadi")
        elif password1.strip() != password2.strip():
            flash("Prollar mos kiritilmadi")
        else:
            user = Users()
            user.fullName = fullname.title()
            user.username = username.strip().lower()
            user.password = bcrypt.hashpw(password1.strip().encode(), bcrypt.gensalt())
            db.session.add(user)
            db.session.commit()
            flash("Ro'yxatdan o'tdingiz")
            return redirect(url_for("login_view"))

    return render_template("admin/register.html")