# Import statements
from flask import Blueprint, request, session, render_template, redirect, url_for
import datetime
import cgi, os, urllib
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
from flask_login import login_required, current_user
from src.services.employee_services.create_request_services import create_request
from src.services.employee_services import delete_request_services
# Import info-level and warning-level loggers from logger.py
from src.logger import info_logger, my_logger

# Define the blueprint, this blueprint is meant for routes specifically for employees only, like submitting or deleting
# a reimbursement request
employee_blueprint = Blueprint('employee_blueprint', __name__)

# Route for submitting a new request, works for both filling out the input field or uploading a text file
@employee_blueprint.route('/requests/submit', methods=['POST'])
@login_required
def submit_request():
    # First verify the session is of account_type Employee
    if session['account_type'] == 'Employee':
        # If the employee submitted the input form, then request.form.get('amount') will exist and the if block
        # executes
        if request.form.get('amount'):
            # Gather amount and reason from the form data, date time is the time of the submission, status is default
            # to pending, get employee information from current_user and call the create_request service method,
            # finally, redirect back to the requests page
            amount = request.form.get('amount')
            reason = request.form.get('reason')
            datetimenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = 'pending'
            employee_first_name = current_user._first_name
            employee_last_name = current_user._last_name
            employee_id = current_user.get_employee_id()
            manager_id = current_user.get_manager_id()
            create_request(employee_id, amount, reason, datetimenow, status, manager_id,
                           employee_first_name, employee_last_name)
            info_logger.info('Employee has created a new request')
            return redirect(url_for('user_blueprint.requests'))

        # If the employee uploaded the file, then request.form.get('amount') won't exist and the else block executes
        # instead
        else:
            try:
                from src.app import app
                # Get the file from the request with .files, 'filename' is the name of the input
                fileitem = request.files['filename']
                # Path to temporarily save the file onto the server, uses .join to add the file name onto the directory
                fileitem.save(os.path.join(app.config['IMAGE_UPLOADS'], fileitem.filename))
                # Read from the file, add the \ again to add the file name to the directory
                file_read = open(app.config['IMAGE_UPLOADS'] + """\\""" + fileitem.filename, 'r')
                # Amount must be in the second line, directly after the $ symbol, and must be an integer otherwise
                # int(amount) raises the ValueError
                lines = file_read.readlines()
                amount = lines[1][1:].rstrip('\n')
                int(amount)
                # Reason must be in the 4th line
                reason = lines[3].rstrip('\n')
                # Close the file and delete the uploaded file off the server
                file_read.close()
                os.remove(app.config['IMAGE_UPLOADS'] + """\\""" + fileitem.filename)
                datetimenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                status = 'pending'
                # date time is the time of the submission, status is default to pending, get employee information
                # from current_user and call the create_request service method, finally redirect back to the
                # requests page
                employee_first_name = current_user._first_name
                employee_last_name = current_user._last_name
                employee_id = current_user.get_employee_id()
                manager_id = current_user.get_manager_id()
                create_request(employee_id, amount, reason, datetimenow, status, manager_id,
                               employee_first_name, employee_last_name)
                info_logger.info('Employee has created a new request')
                return redirect(url_for('user_blueprint.requests'))
            # If the amount is not an integer, ValueError is raised, redirect them back to the requests page
            except ValueError:
                my_logger.error('Inputted amount was not an integer')
                return redirect(url_for('user_blueprint.requests', submit='True'))

# Route to delete any number of requests, via the checkbox form
@employee_blueprint.route('/requests/delete', methods=['POST'])
@login_required
def delete_request():
    # Acquire the form data as a list to be iterated over
    list_of_deletions = request.form.getlist('delete-request')
    for deletion in list_of_deletions:
        # Delimit the list item by - (it appears as reimbursement_id-employee_id ie 1-0), call the service method
        reimbursement_id = deletion.split('-')[0]
        employee_id = deletion.split('-')[1]
        delete_request_services.delete_request(reimbursement_id, employee_id)
    info_logger.info('Employee has deleted from their reimbursements')
    return redirect(url_for('user_blueprint.requests'))