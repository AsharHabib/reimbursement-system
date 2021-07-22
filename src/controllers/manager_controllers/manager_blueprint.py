# Import statements, relevant service functions
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from src.services.employee_services.check_employee_exists_services import check_employee_exists
from src.services.manager_services.create_employee_account_services import create_employee_account
from src.services.manager_services import update_status_services
from src.services.manager_services.delete_employee_services import delete_employee
# Import info-level and warning-level loggers from logger.py
from src.logger import info_logger, my_logger

# Define the manager_blueprint, meant for routes that only managers have access to
manager_blueprint = Blueprint('manager_blueprint', __name__)

# Route for the signup page to create a new employee account
@login_required
@manager_blueprint.route('/signup')
def signup():
    try:
        # If manager, go to signup page, if employee tries going to /signup, redirect them to profile
        if session['account_type'] == 'Manager':
            info_logger.info('Manager used /signup route')
            return render_template('signup.html')
        elif session['account_type'] == 'Employee':
            my_logger.warning('Employee attempted to use /signup')
            return redirect(url_for('main_blueprint.profile'))
    # This except block catches KeyErrors that occur if someone is not logged in, thus session['account_type']
    # does not exist yet and that would raise the KeyError, send back to pre_login
    except KeyError:
        my_logger.error('User attempted /signup without being logged in')
        return redirect(url_for('auth.pre_login'))

# Route for the signup form to send form data to
@login_required
@manager_blueprint.route('/employees/create', methods=['POST'])
def signup_post():
    # Get manager ID from current_user, and all the form data back
    manager_id = current_user.get_manager_id()
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    password = request.form.get('password')
    job_title = request.form.get('job_title')
    # If an account with the same username and password exists, flash a message and go back to the signup page
    if check_employee_exists(username, password):
        flash('That account already exists.')
        my_logger.warning('Manager attempted to input an account that already exists')
        return redirect(url_for('manager_blueprint.signup'))
    # If that account doesn't already exist, create the account with the service method, flash a message and go
    # back to the profile
    create_employee_account(manager_id, first_name, last_name, username, password, job_title)
    flash('New employee account created!')
    info_logger.info('Manager successfully created a new employee account')
    return redirect(url_for('main_blueprint.profile'))

# Route to delete any number of employee accounts, based on the checkboxes that are checked
@login_required
@manager_blueprint.route('/employees/delete', methods=['POST'])
def delete_employees():
    # Acquire the form data as a list to be iterated over
    list_of_deletions = request.form.getlist('delete-employees')
    # Iterate over the list and delete each employee, go back to the profile page after
    for deleted_employee in list_of_deletions:
        delete_employee(deleted_employee)
        info_logger.info('Manager successfully deleted Employee #{}'.format(deleted_employee))
    return redirect(url_for('main_blueprint.profile'))

# Route to handle the updated requests form
@manager_blueprint.route('/requests', methods=['POST'])
@login_required
def update_status():
    # If the session is of account type 'Manager', do the if block
    if session['account_type'] == 'Manager':
        # length/2 of the form because each reimbursement request has two inputs, 1 for status and 1 for message
        # Convert that number to an int because dividing by 2 returns a decimal like 6.0
        num_requests = int(len(request.form)/2)
        # Get the keys and values from the form
        keys = list(request.form.keys())
        values = list(request.form.values())
        for req in range(num_requests):
            # The status looks like 'status-reimbursement_id-employee_id-manager_id' e.g. 'status-1-0-0'
            # So delimit by '-' and assign to the respective IDs
            full_key_status = keys[req*2]
            reimbursement_id = full_key_status.split('-')[1]
            employee_id = full_key_status.split('-')[2]
            manager_id = full_key_status.split('-')[3]
            # Status refers to every even value, message to each odd value
            status = values[req*2]
            manager_message = values[req*2 + 1]
            if not manager_message:
                # If the message was null, set it to 'N/A'
                manager_message = 'N/A'
            # Finally update the request with the new status and message, return to requests page after finishing the
            # for loop
            update_status_services.update_status(reimbursement_id, employee_id, manager_id, status, manager_message)
        info_logger.info("Manager updated their employees' reimbursement requests")
        return redirect(url_for('user_blueprint.requests'))
    elif session['account_type'] == 'Employee':
        # If an employee attempts to go here they're redirected to the profile page
        my_logger.warning('Employee attempted to post to /requests')
        return redirect(url_for('main_blueprint.profile'))

# Route for the statistics page, if an employee attempts to go here they're redirected to the profile page
@manager_blueprint.route('/statistics')
@login_required
def statistics():
    if session['account_type'] == 'Manager':
        info_logger.info('Manager went to /statistics')
        return render_template('statistics.html')
    elif session['account_type'] == 'Employee':
        my_logger.warning('Employee attempted to use /statistics route')
        return redirect(url_for('main_blueprint.profile'))