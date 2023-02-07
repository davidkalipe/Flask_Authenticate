from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:140809010@localhost:5432/devoirpy2'

    db.init_app(app)

    loging_manager = LoginManager()
    loging_manager.login_view = 'auth.login'
    loging_manager.init_app(app)

    from project.models import User

    @loging_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



