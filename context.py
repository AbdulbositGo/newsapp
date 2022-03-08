from config import app
from falchemy  import qsort
from models import Author, Category, News

@app.context_processor
def categorys_context():
    categorys = Category.query.all()
    return {"categorys": categorys}

@app.context_processor
def author_context():
    authors = Author.query.all()
    return {"authors": authors}

@app.context_processor
def more_views_context():
    news = News.query.order_by(News.views.desc()).all()
    return {"more_views": news[:3]}