# Generated by Django 4.1.1 on 2022-10-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0002_alter_booking_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='public_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='eventcentre',
            name='public_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='eventcentrecategory',
            name='public_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='public_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hallpaymentcategory',
            name='public_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]