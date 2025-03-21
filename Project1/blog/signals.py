from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


@receiver(post_save, sender=User, dispatch_uid='send_welcome_email')
def send_welcome_email(sender, instance, created, **kwargs):
    print('signal fired')
    if created:  # A flag to see if a new record is created or not.
        send_mail(
            'Welcome',
            'Thanks for registering on our bloggin site',
            'harsh.rana@simformsolutions.com',  # From
            [instance.email],  # To-list
            fail_silently=False
        )
