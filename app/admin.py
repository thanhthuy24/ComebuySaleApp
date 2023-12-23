from flask_admin import Admin
from app.models import Category, Product
from app import app, db

admin = Admin(app=app)