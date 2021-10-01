# Generated by Django 3.2.7 on 2021-09-16 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_database', '0005_customer_email_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailstatus',
            options={'ordering': ['create_status']},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email_status',
        ),
        migrations.RemoveField(
            model_name='emailstatus',
            name='already_sent',
        ),
        migrations.AddField(
            model_name='emailstatus',
            name='create_status',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
