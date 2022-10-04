from email.policy import default
from django.db.models import Q
from django.db import models
from account.models import CustomUser 
# Create your models here.




class EventCentreCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True , blank=True )
    created_at = models.DateTimeField(auto_now_add=True)       

    def __str__(self) -> str:
        return self.name



# Custom QuerySet manager for searching of centre
class EventCentreQuerySet(models.QuerySet):
    def search(self, query ):
        q = Q(name__icontains=query) | Q(description__icontains=query) |  Q(category__name__icontains=query)
        return self.filter(q)


class EventCentreManager(models.Manager):
    def get_queryset(self): 
        return EventCentreQuerySet(self.model , using=self._db)

    def search(self , query):
        return self.get_queryset().search(query)





class EventCentre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True , blank=True )
    location = models.CharField(max_length=100)
    description = models.TextField() 
    stars = models.PositiveIntegerField(default=10)
    is_active = models.BooleanField(default=True)
    # category = models.ManyToManyField(EventCentreCategory)
    created_at = models.DateTimeField(auto_now_add=True)     


    objects =  EventCentreManager()


    def __str__(self) -> str:
        return self.name


    @property
    def images(self):
        return EventCentreImage.objects.filter(event_centre__id=self.id)


    @property
    def hall(self):
        return Hall.objects.filter(event_center__id=self.id)


def upload_to(instance, filename):
    return 'events/{filename}'.format(filename=filename)

class EventCentreImage(models.Model):
    image = models.ImageField(upload_to=upload_to)
    event_centre = models.ForeignKey(EventCentre, on_delete=models.CASCADE, related_name='centre_image')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.event_centre.name

class Hall(models.Model):
    AVAILABILITY_STATUS = (
        ('open', 'open'),
        ('close','close'),
    )
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True , blank=True )
    price = models.PositiveIntegerField()
    has_payment_category = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=10 , default='open' , choices=AVAILABILITY_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    event_centre = models.ForeignKey(EventCentre, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name

    # @property
    # def image(self):
    #     return HallImage.objects.filter(hall__id=self.id)

class HallPaymentCategory(models.Model):
    CATEGORY_TYPE = (
        ('weekday', 'weekday'),
        ('weekend','weekend'),
        ('festive_period','festive_period'),
    )
    type = models.CharField(max_length=20 , choices=CATEGORY_TYPE)
    price = models.PositiveIntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Hall payment Categories'

    def __str__(self) -> str:
        return self.type


def upload_to_hall(instance, filename):
    return 'halls/{filename}'.format(filename=filename)

class HallImage(models.Model):
    image = models.ImageField(upload_to=upload_to_hall)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.hall.name


class Booking(models.Model):
    access_ref = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.DateField()
    expired_date = models.DateField(null=True, blank=True)
    hall = models.ForeignKey(Hall ,on_delete=models.SET_NULL, null=True , related_name='hall_booked')
    payment_status = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL , null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} , {self.hall.name} , {self.event_date}'


