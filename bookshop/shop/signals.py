from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Client


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Client.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profileuser(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
        print('Profile is created!')


# post_save.connect(create_profileuser, sender=User)


@receiver(post_save, sender=User)
def update_profileuser(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile is updated!')


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Client.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
