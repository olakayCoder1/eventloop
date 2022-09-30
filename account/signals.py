import string , random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import CustomUser
from rest_framework.authtoken.models import Token

def random_string_generator(size=10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance , new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.first_name)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = '{slug}-{randstr}'.format(
            slug=slug[:max_length-5], randstr= random_string_generator(size=4)
        )
        return unique_slug_generator(instance,new_slug=new_slug)
    return slug



@receiver(post_save , sender=CustomUser)
def user_profile_signal(sender, instance , created , **kwarg):
    if created:
        Token.objects.create(user=instance)
        instance.slug = unique_slug_generator(instance)
        instance.save()
