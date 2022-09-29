from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    EventCentre , EventCentreCategory 
)
from account.signals import unique_slug_generator



@receiver(post_save , sender=EventCentreCategory)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()


@receiver(post_save , sender=EventCentre)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()
