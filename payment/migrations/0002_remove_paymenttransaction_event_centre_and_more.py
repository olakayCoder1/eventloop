# Generated by Django 4.1.1 on 2022-09-30 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0002_alter_eventcentreimage_event_centre'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='event_centre',
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='centre.booking'),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('success', 'success'), ('failed', 'failed')], default='pending', max_length=10),
        ),
    ]
