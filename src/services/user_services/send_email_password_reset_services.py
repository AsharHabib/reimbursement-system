# Import relevant DAO and call it in the service function
from flask import url_for
# Import info-level logger from logger.py
from src.logger import info_logger
from src.dao.user_dao import send_email_password_reset_dao

def send_email_password_reset(username, account_type, productionDB=True):
    from src.app import mail, serializer, Message
    if account_type == 'manager':
        manager_email = send_email_password_reset_dao.send_email_password_reset(username, account_type, productionDB)
        # Create a token using the serializer and salt is 'email-confirm'
        # Create a message object for the email title, sender, and recipient(s), create the link to
        # go to auth.reset_form (page to actually make a new password), give that link the token and
        # other variables, set the message body and send it
        token = serializer.dumps(manager_email, salt='email-confirm')
        message = Message('Reset Password - Mifflin Dunder', sender='hr@mifflindunder.com',
                          recipients=[manager_email])
        link = url_for('auth.reset_form', token=token, _external=True, is_employee=False, username=username)
        message.body = """Your link is {}. If you did not request this password change, please
                                check your security settings""".format(link)
        mail.send(message)

        # Similar to above but account_type is 'employee'
    elif account_type == 'employee':
        employee_email = send_email_password_reset_dao.send_email_password_reset(username, account_type, productionDB)
        token = serializer.dumps(employee_email, salt='email-confirm')
        message = Message('Reset Password - Mifflin Dunder', sender='hr@mifflindunder.com',
                          recipients=[employee_email])
        link = url_for('auth.reset_form', token=token, _external=True, is_employee=True, username=username)
        message.body = """Your link is {}. If you did not request this password change, please
                                check your security settings""".format(link)
        mail.send(message)
    info_logger.info('{} forgot their password, email has been sent'.format(username))