from flask import Flask
from pathlib import Path
import os


app = Flask(__name__)

OS_UPLOAD_PATH = os.path.join("static", "upload", "images")
IMAGES_UPLOAD_DIR = Path(OS_UPLOAD_PATH)

if not IMAGES_UPLOAD_DIR.exists():
    os.makedirs(IMAGES_UPLOAD_DIR)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = b"opi3iwr90.;q8{dfgIO{@I(oepri[qewiPI{IO[weiq//po"