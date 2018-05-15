# Generated by Django 2.0.5 on 2018-05-15 06:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0004_auto_20180511_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='contact_phone_no',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid Mobile Number !!!', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid Mobile Number !!!', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
