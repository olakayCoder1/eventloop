# Generated by Django 4.0.4 on 2022-09-30 00:16

import centre.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stars', models.PositiveIntegerField(default=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventCentreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventCentreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=centre.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.eventcentre')),
            ],
        ),
        migrations.AddField(
            model_name='eventcentre',
            name='category',
            field=models.ManyToManyField(to='centre.eventcentrecategory'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_ref', models.CharField(blank=True, max_length=100, null=True)),
                ('event_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('paid', models.BooleanField(default=False)),
                ('event_centre', models.ManyToManyField(related_name='event_centre', to='centre.eventcentre')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
