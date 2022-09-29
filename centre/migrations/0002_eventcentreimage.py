# Generated by Django 4.0.4 on 2022-09-29 16:38

import centre.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCentreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=centre.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.eventcentre')),
            ],
        ),
    ]
