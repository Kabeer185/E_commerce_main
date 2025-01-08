

from django.core.mail import send_mail

from django.conf import settings 


def send_forget_password_mail(email , token):
    subject = 'Your forget password link'
    message = f'hi, click on the link to reset your password http://127.0.0.1:8000/change_password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_email_to_user(email):
    subject = 'Order Confirmation'
    message = f"""
    Hi,

    Thank you for your order! Your payment has been successfully processed.


    We appreciate your business and will keep you updated on the status of your order.

    Best regards,
    Your E-Commerce Team
    """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
