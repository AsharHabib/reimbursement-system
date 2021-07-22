# Import relevant DAO and call it in the service function
from src.dao.manager_dao import send_email_manager_username_dao
# Import info-level logger from logger.py
from src.logger import info_logger

# Create a message object for the email title, sender, and recipient(s),
# set the message body and send it
def send_email_manager_username(first_name, last_name):
    from src.app import mail, Message
    username, email = send_email_manager_username_dao.send_email_manager_username(first_name, last_name)
    message = Message('Resend Username - Mifflin Dunder', sender='hr@mifflindunder.com',
                      recipients=[email])
    message.body = """Your username is {}.""".format(username)
    mail.send(message)
    info_logger.info('{} {} forgot their username, email has been sent'.format(first_name, last_name))