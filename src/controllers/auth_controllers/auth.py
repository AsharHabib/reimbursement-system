# All import statements
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from src.services.employee_services.check_employee_exists_services import check_employee_exists
from flask_login import login_user, logout_user, login_required, current_user
from src.services.employee_services.get_employee_first_last_names_services import get_employee_first_last_names
from src.services.employee_services.send_email_employee_username_services import send_email_employee_username
from src.services.manager_services.check_manager_exists_services import check_manager_exists
from src.services.employee_services.make_employee_object_services import make_employee_object
from src.services.manager_services.get_manager_first_last_names_services import get_manager_first_last_names
from src.services.manager_services.make_manager_object_services import make_manager_object
from src.services.manager_services.send_email_manager_username_services import send_email_manager_username
from src.services.user_services.get_all_usernames_services import get_all_usernames
from src.services.user_services.reset_password_services import reset_password
from src.services.user_services.send_email_password_reset_services import send_email_password_reset
from src.logger import my_logger, info_logger
import pyotp, os

# Create the auth blueprint, primarily for routes that can be accessed before logging in
auth = Blueprint('auth', __name__)

# Pre-login page for the user to choose logging in as employee or manager
@auth.route('/pre_login')
def pre_login():
    # current_user.is_authenticated() always returns True but the current_user must already exist, try sending
    # them back to their profile, if they don't exist it will raise a TypeError and that means no user is logged
    # in yet, then render to the pre_login.html page, which has two links with varying query arg values
    # i.e. ?is_employee=True or False
    try:
        if current_user.is_authenticated():
            my_logger.warning('Logged in user attempted to login again')
            return redirect(url_for('main_blueprint.profile'))
    except TypeError:
        info_logger.info('User went to the pre login page')
        return render_template('pre_login.html')


# Route for actually logging in
@auth.route('/login')
def login():
    try:
        # If the user is already logged in, redirect to their profile, else this raises a TypeError which is
        # caught below
        if current_user.is_authenticated():
            my_logger.warning('Logged in user attempted to login again')
            return redirect(url_for('main_blueprint.profile'))
    except TypeError:
        # Get the query argument, if it's 'True', send to employee's login page, else if it's 'False' send to
        # manager login's page, else just go to the pre-login
        is_employee = request.args.get('is_employee')
        if is_employee == 'True':
            info_logger.info('User directed to login as employee')
            return render_template('employee_login.html')
        elif is_employee == 'False':
            info_logger.info('User directed to login as manager')
            return render_template('manager_login.html')
        else:
            my_logger.error('Unidentified query value passed in for is_employee')
            return redirect(url_for('auth.pre_login'))

# The employee_login form posts to here, get the username and password from the form and check they exist
@auth.route('/login/employee', methods=['POST'])
def login_post_employee():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    if not check_employee_exists(username, password):
        # If they don't exist, flash the message and redirect to the login page with is_employee=True
        flash('Please check your log in details and try again.')
        my_logger.warning('Employee account did not exist')
        return redirect(url_for('auth.login', is_employee=True))
    # If the employee exists, redirect to the two_factor page, query arg the username, account type and function call
    info_logger.info('Employee sent to 2 Factor page')
    return redirect(url_for('auth.two_factor', username=username, account_type='Employee', function_call='login'))

# The manager_login form posts to here, get the username and password from the form and check they exist
@auth.route('/login/manager', methods=['POST'])
def login_post_manager():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    if not check_manager_exists(username, password):
        # If they don't exist, flash the message and redirect to the login page with is_employee=False
        flash('Please check your log in details and try again.')
        my_logger.warning('Manager account did not exist')
        return redirect(url_for('auth.login', is_employee=False))
    # If the manager exists, redirect to the two_factor page, query arg the username, account type and function call
    info_logger.info('Manager sent to 2 Factor page')
    return redirect(url_for('auth.two_factor', username=username, account_type='Manager', function_call='login'))

@auth.route('/2fa')
def two_factor():
    # Create session keys that can be picked up in the two_factor_form function
    session['username'] = request.args.get('username')
    session['account_type'] = request.args.get('account_type')
    session['function_call'] = request.args.get('function_call')
    info_logger.info('User lands on 2 Factor page')
    return render_template("two_factor.html")

@auth.route("/2fa/", methods=["POST"])
def two_factor_form():
    # Get back the session keys and pop username, function_call; account_type still needed if user is logging in
    username = session['username']
    account_type = session['account_type']
    function_call = session['function_call']
    session.pop('username')
    session.pop('function_call')
    # getting secret key used by user
    secret = os.environ['SECRET_KEY']
    # getting OTP provided by user
    otp = int(request.form.get("otp"))
    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # This block is for if function_call is 'login' i.e. the route was redirected from the login post function
        if function_call == 'login':
            # inform users if OTP is valid
            flash("The TOTP 2FA token is valid", "success")
            # Differentiate between employee or manager logging in, log the user in
            if account_type == 'Employee':
                login_user(make_employee_object(username))
                info_logger.info('Employee logged in')
                return redirect(url_for("main_blueprint.profile"))
            elif account_type == 'Manager':
                login_user(make_manager_object(username))
                info_logger.info('Manager logged in')
                return redirect(url_for("main_blueprint.profile"))
        elif function_call == 'reset':
            # Pop account_type from session, it's no longer needed
            session.pop('account_type')
            # This block is for if function_call is 'reset' i.e. the route was redirected from the reset function
            flash("The TOTP 2FA token is valid", "success")
            # Differentiate between employee or manager resetting password, send email
            if account_type == 'Employee':
                send_email_password_reset(username, 'employee')
                info_logger.info('Reset password email sent for employee')
                return '<h2 id="h2-header">An email has been sent to you to reset your password, the link expires in 1 hour.</h2>'
            elif account_type == 'Manager':
                send_email_password_reset(username, 'manager')
                info_logger.info('Reset password email sent for manager')
                return '<h2 id="h2-header">An email has been sent to you to reset your password, the link expires in 1 hour.</h2>'
        else:
            my_logger.error('Function that called 2 Factor POST is undefined')
            return redirect(url_for("auth.pre_login"))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        my_logger.warning('Invalid 2FA token submitted')
        return redirect(url_for("auth.two_factor", username=username, account_type=account_type, function_call=function_call))

# Route for resending the username through email in case you forget it, checks the is_employee query arg
# and renders the correct template, else it defaults to the pre-login page
@auth.route('/resend')
def resend_user():
    is_employee = request.args.get('is_employee')
    if is_employee == 'True':
        info_logger.info('User sent to Employee resend user page')
        return render_template('resend_user_employee.html')
    elif is_employee == 'False':
        info_logger.info('User sent to Manager resend user page')
        return render_template('resend_user_manager.html')
    else:
        my_logger.warning('Invalid query value sent for is_employee')
        return redirect(url_for('auth.pre_login'))

# Used when user submits the form for first and last name
@auth.route('/resend', methods=['POST'])
def resend_user_post():
    # Convert from string to boolean
    is_employee = request.args.get('is_employee')
    if is_employee == 'True':
        is_employee = True
    elif is_employee == 'False':
        is_employee = False
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    # Need try-except block because if first or last name doesn't exist in manager_first_names/manager_last_names,
    # the .index() will raise a ValueError
    try:
        # If the names correspond to an employee, get all employee first and last names, check that the first and last
        # names given are at the same index of the respective tuples, if not that means that both names exist but don't
        # match, in that case flash a message and redirect back to resend_user route
        if is_employee:
            employee_first_names, employee_last_names = get_employee_first_last_names()
            if employee_first_names.index(first_name) == employee_last_names.index(last_name):
                send_email_employee_username(first_name, last_name)
                info_logger.info('Email sent to {} {} for their username'.format(first_name, last_name))
            else:
                flash("Those names do not match, try again.")
                my_logger.warning('The names did not match')
                return redirect(url_for('auth.resend_user', is_employee=True))
        else:
            # If the names correspond to a manager, get all manager first and last names, check that the first and last
            # names given are at the same index of the respective tuples, if not that means that both names exist but
            # don't match, in that case flash a message and redirect back to resend_user route
            manager_first_names, manager_last_names = get_manager_first_last_names()
            if manager_first_names.index(first_name) == manager_last_names.index(last_name):
                send_email_manager_username(first_name, last_name)
                info_logger.info('Email sent to {} {} for their username'.format(first_name, last_name))
            else:
                flash("Those names do not match, try again.")
                my_logger.warning('The names did not match')
                return redirect(url_for('auth.resend_user', is_employee=False))
        # Simple HTML message
        return '<h1 id="h1-header">Your username has been sent to your email.</h1>'
    # If one or both names are not legit, the ValueError is raised and caught here, flash a message and redirect back
    # to resend_user
    except ValueError:
        flash("One of those names does not exist, try again.")
        my_logger.error('One or both names did not exist')
        return redirect(url_for('auth.resend_user', is_employee=is_employee))

# Route for resetting an account's password
@auth.route('/reset')
def reset_pass():
    info_logger.info('User wishes to reset their password')
    return render_template('reset_pass.html')

# Before being able to reset a password, check that the entered username exists in either table, if so then we are set
# to try a 2 factor authentication, else flash a message and redirect back to reset_pass
@auth.route('/reset', methods=['POST'])
def reset_pass_post():
    username = request.form.get('username')
    manager_usernames, employee_usernames = get_all_usernames()
    if username in manager_usernames:
        info_logger.info('Manager sent to 2 Factor page')
        return redirect(url_for('auth.two_factor', username=username, account_type='Manager', function_call='reset'))
    elif username in employee_usernames:
        info_logger.info('Employee sent to 2 Factor page')
        return redirect(url_for('auth.two_factor', username=username, account_type='Employee', function_call='reset'))
    else:
        flash("That username does not exist, try again.")
        my_logger.error('The given username did not exist')
        return redirect(url_for('auth.reset_pass'))

# Route that exists in the email sent for resetting password, has a token in the URI which gets a time limit here
@auth.route('/reset/<token>')
def reset_form(token):
    from src.app import SignatureExpired, serializer
    is_employee = request.args.get('is_employee')
    if is_employee == 'True':
        is_employee = True
    elif is_employee == 'False':
        is_employee = False
    username = request.args.get('username')
    try:
        # Time limit of 3600 seconds, or 1 hour, create two session keys to be used in the post method below
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
        session['is_employee'] = is_employee
        session['username'] = username
        info_logger.info('Token still valid, user presented with reset form page')
        return render_template('reset_form.html')
    except SignatureExpired:
        # If the token expires, return the HTML h1 tag
        my_logger.error('Password reset token has expired')
        return '<h1 id="h1-header">The token has expired.</h1>'

# Route for resetting the password after submitting the form
@auth.route('/reset_post', methods=['POST'])
def reset_form_post():
    # Convert is_employee to a boolean
    is_employee = request.args.get('is_employee')
    if is_employee == 'True':
        is_employee = True
        account_type = 'employee'
    elif is_employee == 'False':
        is_employee = False
        account_type = 'manager'
    else:
        is_employee = True
        account_type = 'employee'
    # Get username from the query args, new and confirmed passwords from the form, pop the session keys set in
    # reset_form
    username = request.args.get('username')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    session.pop('is_employee')
    session.pop('username')
    # Call service function if the passwords match, else resend the email and return an h1 tag
    if new_password == confirm_password:
        reset_password(new_password, username, is_employee)
        info_logger.info('User has reset their password')
    else:
        send_email_password_reset(username, account_type)
        my_logger.warning('The passwords did not match, new email was sent')
        return """<h1 id="h1-header">The passwords did not match, we've sent you another email.</h1>"""
    # try-except block in case this route gets called after being logged in (this option exists in the /settings page)
    try:
        if current_user.is_authenticated():
            info_logger.info('Logged in user sent to their profile')
            return redirect(url_for('main_blueprint.profile'))
    except TypeError:
        info_logger.info('Logged out user sent to the login page')
        return redirect(url_for('auth.login', is_employee=is_employee))

# Route to log out
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    info_logger.info('User has logged out')
    return redirect(url_for('main_blueprint.index'))