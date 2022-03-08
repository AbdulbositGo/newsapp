from config import app
from models import *

from error_handler import *
from admin_panel import *
from context import *
from client import *
from login import *

if __name__ == "__main__":
    app.run(debug=True)