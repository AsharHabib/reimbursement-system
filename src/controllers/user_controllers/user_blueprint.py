# Import statements
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, Response
from flask_login import login_required, current_user
from src.services.employee_services.get_reimbursements_under_employee_services import get_reimbursements_under_employee
from src.services.manager_services.get_reimbursements_under_manager_services import get_reimbursements_under_manager
from json import dumps
from src.models.reimbursement import ReimbursementEncoder
# Import info-level logger from logger.py
from src.logger import info_logger

# Create the user blueprint, meant for routes that are accessible for any account that is logged in
user_blueprint = Blueprint('user_blueprint', __name__)

# For pulling up requests, login is required and can be used by both account types, specifically for requests
@user_blueprint.route('/requests')
@login_required
def requests():
    # If the account type is 'Manager' send to the employee_requests page, else if it's 'Employee' but there is
    # no submit query argument, go to the made_requests page, if there is a submit query arg, go to the
    # submit-request page
    if session['account_type'] == 'Manager':
        info_logger.info('Manager used /requests route')
        return render_template('employee_requests.html')
    elif session['account_type'] == 'Employee' and not request.args.get('submit'):
        info_logger.info('Employee used /requests route')
        return render_template('made_requests.html')
    elif session['account_type'] == 'Employee' and request.args.get('submit'):
        info_logger.info('Employee used /requests route to submit')
        return render_template('submit_request.html')

# JSON route used by employee_requests.js, made_requests.js, and statistics.js JS scripts. Used to get
# data on reimbursement requests
@user_blueprint.route('/requests.json')
@login_required
def requests_json():
    # If the account type is Manager, call the service method for getting all reimbursements under a manager
    # then json.dumps that with the JSON encoder, return that JSON
    if session['account_type'] == 'Manager':
        manager_id = current_user.get_manager_id()
        reimbursements_dict = get_reimbursements_under_manager(manager_id)
        my_json = dumps(reimbursements_dict, cls=ReimbursementEncoder)
        info_logger.info('Reimbursements under Manager #{} returned as JSON'.format(manager_id))
        return Response(my_json, status=200)
    if session['account_type'] == 'Employee':
        # If the account type is Employee, call the service method for getting all reimbursements under an employee
        # then json.dumps that with the JSON encoder, return that JSON
        first_name = current_user._first_name
        last_name = current_user._last_name
        employee_id = current_user.get_employee_id()
        manager_id = current_user.get_manager_id()
        reimbursements_dict = get_reimbursements_under_employee(employee_id, manager_id, first_name, last_name)
        my_json = dumps(reimbursements_dict, cls=ReimbursementEncoder)
        info_logger.info('Reimbursements under Employee #{} returned as JSON'.format(employee_id))
        return Response(my_json, status=200)