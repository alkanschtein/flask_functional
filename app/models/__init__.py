from .base import db
from flask_migrate import Migrate

# Add tables
from .User import User


def init_app(app):
    db.init_app(app)


def migrate(app):
    return Migrate(app, db)