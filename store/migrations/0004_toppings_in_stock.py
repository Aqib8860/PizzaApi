# Generated by Django 3.1.4 on 2021-05-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210501_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppings',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
