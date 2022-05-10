from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.secret_key = 'temporary_passkey'
    # app.secret_key = os.urandom(24).hex()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel123.sqlite'
    db.init_app(app)

    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app
