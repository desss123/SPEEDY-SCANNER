# Generated by Django 2.2 on 2020-07-18 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200718_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_date',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
    ]
