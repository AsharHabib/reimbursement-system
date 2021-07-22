# Import statements from flask, json.dumps, relevant service functions
from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from json import dumps
from src.services.manager_services.get_employees_under_manager_services import get_employees_under_manager
from src.services.user_services.send_email_password_reset_services import send_email_password_reset
# Import info-level logger from logger.py
from src.logger import info_logger

# Define the main_blueprint, used for routes that are available to employees and managers after logging in
main_blueprint = Blueprint('main_blueprint', __name__)

# Home route
@main_blueprint.route('/')
def index():
    info_logger.info('User went to the home page')
    return render_template('index.html')

#Profile route, login required, sends to profile.html which checks session['account_type']
@main_blueprint.route('/profile')
@login_required
def profile():
    if session['account_type']:
        info_logger.info('Logged in user went to profile page')
        return render_template('profile.html')

# JSON route used by profile.js, for the profile page of both managers and employees
@main_blueprint.route('/profile.json')
@login_required
def profile_json():
    # If the session is of account type 'Manager' then the if block runs, gets first name, last name, username,
    # password, and manager ID from current_user, and the service function returns lists for employees under the
    # specific manager, json.dumps the dictionary that puts all the data together
    if session['account_type'] == 'Manager':
        first_name = current_user._first_name
        last_name = current_user._last_name
        # Getting username and password if for some reason I want them later
        username = current_user._username
        password = current_user._password
        manager_id = current_user.get_manager_id()
        employee_ids, employee_first_names, employee_last_names, job_titles = get_employees_under_manager(manager_id)
        json_dict = {'first_name':first_name, 'last_name':last_name, 'username':username, 'password':password,
                     'manager_id':manager_id, 'employee_ids':employee_ids, 'employee_first_names':employee_first_names,
                     'employee_last_names':employee_last_names, 'job_titles':job_titles}
        info_logger.info('Profile data for Manager has been JSONified')
        return dumps(json_dict)
    # If the session is of account_type 'Employee', only need first name, last name, manager id, and job title
    # from current_user, json.dumps the dictionary that puts all the data together
    if session['account_type'] == 'Employee':
        first_name = current_user._first_name
        last_name = current_user._last_name
        manager_id = current_user.get_manager_id()
        job_title = current_user._job_title
        json_dict = {'first_name': first_name, 'last_name': last_name, 'manager_id': manager_id, 'job_title':job_title}
        info_logger.info('Profile data for Employee has been JSONified')
        return dumps(json_dict)

# Settings route
@main_blueprint.route('/settings')
@login_required
def settings():
    info_logger.info('Logged in user has gone to /settings')
    return render_template('settings.html')

# Route for resetting the password AFTER logging in, so this one doesn't need a 2 Factor Authorization, simply call the
# service function to send the email
@main_blueprint.route('/settings/reset')
@login_required
def reset_pass():
    if session['account_type'] == 'Employee':
        username = current_user._username
        send_email_password_reset(username, 'employee')
    elif session['account_type'] == 'Manager':
        username = current_user._username
        send_email_password_reset(username, 'manager')
    info_logger.info('Email to reset password has been sent')
    return '<h2 id="h2-header">An email has been sent to you to reset your password, the link expires in 1 hour.</h2>'