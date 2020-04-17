# Generated by Django 3.0.5 on 2020-04-17 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200417_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dateadded',
            field=models.DateField(auto_created=True, default=datetime.date(2020, 4, 17)),
        ),
        migrations.AddField(
            model_name='product',
            name='visits',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
