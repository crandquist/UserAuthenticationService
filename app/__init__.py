from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()  # Create a Migrate instance


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Your blueprint registrations and other app setup code here

    return app
