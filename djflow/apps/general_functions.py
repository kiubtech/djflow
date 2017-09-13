from django.core.mail import EmailMultiAlternatives
from djflow.core.json_settings import get_settings

settings = get_settings()


def send_email(subject, to_email, html_content):
    """
    Enviamos un correo con HTML
    """
    msg = EmailMultiAlternatives(subject, html_content, settings['EMAIL']['DEFAULT_FROM_EMAIL'], [to_email])
    msg.content_subtype = "html"
    msg.send()
