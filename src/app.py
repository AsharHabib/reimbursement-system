# Import from various packages, blueprints from all the controllers,
# and the service method for the loading the user after login
import os

from flask import Flask, session, redirect, url_for
from flask_login import LoginManager, logout_user
from src.controllers.manager_controllers.manager_blueprint import manager_blueprint
from src.controllers.employee_controllers.employee_blueprint import employee_blueprint
from src.controllers.user_controllers.user_blueprint import user_blueprint
from src.controllers.main_controllers.main_blueprint import main_blueprint
from src.controllers.auth_controllers.auth import auth
from src.services.user_services.user_load_services import user_load
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from src.logger import my_logger, info_logger

# Create flask app, register all the blueprints, set the config variables
app = Flask(__name__)
app.register_blueprint(employee_blueprint)
app.register_blueprint(manager_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(auth)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['IMAGE_UPLOADS'] = r'{}'.format(os.environ['IMAGE_UPLOADS'])

# Create a LoginManager, default login view, and feed app into it
login_manageragain = LoginManager()
login_manageragain.login_view = 'auth.pre_login'
login_manageragain.init_app(app)

# Create object to handle email, and a serializer for safe and timed tokens
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Load user with the given ID, either employee or manager id
@login_manageragain.user_loader
def load_user(user_id):
    info_logger.debug('User has logged in')
    return user_load(user_id)

# Catch all function for any random endpoints (localhost:5000/randomness)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    my_logger.error('User attempted going to a nonexistent route')
    return redirect(url_for('main_blueprint.index'))