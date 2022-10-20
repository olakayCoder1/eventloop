import string , random
from django.utils.text import slugify



def random_string_generator(size=10, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



"""
THIS FUNCTION GENERATE UNIQUE SLUG FOR THE USER OBJECT
"""
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



"""
THIS FUNCTION GENERATE PUBLIC ID FOR THE USER OBJECT
"""
def unique_public_id_generator(instance , new_public_id=None):
    if new_public_id is not None:
        public_id = new_public_id
    else:
        public_id = random_string_generator(size=10)
    Klass = instance.__class__
    max_length = Klass._meta.get_field('public_id').max_length
    public_id = public_id[:max_length]
    qs_exists = Klass.objects.filter(public_id=public_id).exists()

    if qs_exists:
        new_public_id = '{public_id}-{randstr}'.format(
            public_id=public_id[:max_length-5], randstr= random_string_generator(size=4)
        )
        return unique_public_id_generator(instance,new_public_id=new_public_id)
    return public_id
