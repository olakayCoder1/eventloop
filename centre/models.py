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

# Custom model Manager for searching centre the search uses the following
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
    category = models.ManyToManyField(EventCentreCategory)
    created_at = models.DateTimeField(auto_now_add=True)     


    objects =  EventCentreManager()


    def __str__(self) -> str:
        return self.name


    @property
    def images(self):
        return EventCentreImage.objects.filter(event_centre__id=self.id)


def upload_to(instance, filename):
    return 'events/{filename}'.format(filename=filename)

class EventCentreImage(models.Model):
    image = models.ImageField(upload_to=upload_to)
    event_centre = models.ForeignKey(EventCentre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    access_ref = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.DateField()
    expired_date = models.DateField()
    event_centre = models.ManyToManyField(EventCentre , related_name='event_centre')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL , null=True)
    paid = models.BooleanField(default=False)


