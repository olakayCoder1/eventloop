from django.db import models
from account.models import CustomUser
from centre.models import Booking
# Create your models here.



class PaymentTransaction(models.Model):
    TRANSACTION_STATUS = (
        ('pending', 'pending'),
        ('success','success'),
        ('failed','failed'),
    )
    public_id = models.CharField(max_length=10 , null=True , blank=True)
    user = models.ForeignKey(CustomUser , on_delete=models.SET_NULL , null=True)
    book = models.ForeignKey(Booking , on_delete=models.SET_NULL , null=True)
    amount = models.DecimalField(max_digits=100, null=True , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='pending' , choices=TRANSACTION_STATUS)
    payment_reference = models.CharField(max_length=100, default='', blank=True)


    def __str__(self) -> str:
        return f'{self.book.user.email} , {self.amount} , {self.status}'