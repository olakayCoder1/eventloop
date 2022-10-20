from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    EventCentre , EventCentreCategory ,
    Hall 
)
from account.utils import  random_string_generator , unique_public_id_generator
from django.utils.text import slugify


@receiver(post_save , sender=EventCentreCategory)
def event_centre_category_signal(sender, instance , created , **kwarg):
    if created:
        slug = slugify(instance.name)
        slug_exist = EventCentreCategory.objects.filter(slug=slug).exists()
        if slug_exist:
            new_slug = slug + '-' + random_string_generator(5)
        else:
            new_slug = slug
        instance.slug = new_slug
        instance.public_id = unique_public_id_generator(instance)
        instance.save()


@receiver(post_save , sender=EventCentre)
def event_centre_signal(sender, instance , created , **kwarg):
    if created:
        slug = slugify(instance.name)
        slug_exist = EventCentre.objects.filter(slug=slug).exists()
        if slug_exist:
            new_slug = slug + '-' + random_string_generator(5)
        else:
            new_slug = slug
        instance.slug = new_slug
        instance.public_id = unique_public_id_generator(instance)
        instance.save()



@receiver(post_save , sender=Hall)
def hall_signal(sender, instance , created , **kwarg):
    if created:
        slug = slugify(instance.name)
        slug_exist = Hall.objects.filter(slug=slug).exists()
        if slug_exist:
            new_slug = slug + '-' + random_string_generator(5)
        else:
            new_slug = slug
        instance.slug = new_slug
        instance.public_id = unique_public_id_generator(instance)
        instance.save()
