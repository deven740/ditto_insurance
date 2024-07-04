import os
from dotenv import load_dotenv
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig
from pydantic import EmailStr


load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_NAME = os.getenv("EMAIL_NAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
PASSWORD_RESET_ROUTE = os.getenv("PASSWORD_RESET_ROUTE")
PASSWORD_RESET_ROUTE_LOGIN = os.getenv("PASSWORD_RESET_ROUTE_LOGIN")
ATTACHMENT_PATH = os.getenv("ATTACHMENT_PATH")

conf = ConnectionConfig(
    MAIL_USERNAME=EMAIL,
    MAIL_PASSWORD=EMAIL_PASSWORD,
    MAIL_FROM=EMAIL,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME=EMAIL_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


def send_email(
    policy: dict,
    background_tasks: BackgroundTasks,
):
    """
    Send an email with the specified subject, body, and recipient email.

    Args:
        user_email (EmailStr): The email address of the recipient.
        subject (str): The subject of the email.
        email_body (str): The body content of the email.
        background_tasks (BackgroundTasks): The background tasks instance to add the email sending task.

    Returns:
        None
    """
    body = f"Dear {policy['customer_name']}, your policy of {policy['policy_type']} is Issued, Your policy number is {policy['policy_number']}"
    message = MessageSchema(
        subject="Policy Issued",
        recipients=[policy["email"]],
        body=body,
        subtype=MessageType.html,
    )
    mail = FastMail(conf)

    background_tasks.add_task(mail.send_message, message)
