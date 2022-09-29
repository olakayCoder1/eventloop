from email.message import EmailMessage
import ssl
import smtplib
import os
import environ


env = environ.Env()
environ.Env.read_env()


def send_reset_mail(receiver,token,uuidb64):
    sender_email = env('EMAIL_SENDER')
    receiver_email = receiver
    password = env('EMAIL_PASSWORD') 
    subject = "Paasword reset"
    body = f"""
            we receive a request to reset your password\n
            You can ignore if you don't make the request. Click the link below the to set new password.\n
            http://127.0.0.1:8000/api/v1/auth/setpassword/{token}/{uuidb64}/
        """

    em = EmailMessage()
    em["From"] = receiver_email
    em["To"] = sender_email
    em["subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
            connection.login(sender_email, password)
            connection.sendmail(sender_email, receiver_email, em.as_string())
    except:
        pass
    return True