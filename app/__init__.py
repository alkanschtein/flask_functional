from flask import Flask
from .config import config_creator


def create_app():
    from . import models, routes, services
    app = Flask(__name__)

    # Create Config
    app.config.from_object(config_creator())

    # Models
    models.init_app(app)

    # Database migration
    models.migrate(app)

    # Register blueprints
    routes.init_app(app)

    # TODO services.init_app(app)
    return app
