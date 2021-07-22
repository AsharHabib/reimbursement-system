# Import relevant DAO and call it in the service function
from src.dao.employee_dao import send_email_employee_username_dao
# Import info-level logger from logger.py
from src.logger import info_logger

def send_email_employee_username(first_name, last_name):
    from src.app import mail, Message
    username, email = send_email_employee_username_dao.send_email_employee_username(first_name, last_name)
    # set up the Message object with a title, sender, and recipient, make the message
    # body and send it
    message = Message('Resend Username - Mifflin Dunder', sender='hr@mifflindunder.com',
                      recipients=[email])
    message.body = """Your username is {}.""".format(username)
    mail.send(message)
    info_logger.info('{} {} forgot their username, email has been sent'.format(first_name, last_name))