# Generated by Django 3.1.4 on 2021-05-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210501_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=8),
        ),
        migrations.AlterField(
            model_name='userpizza',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=8),
        ),
        migrations.DeleteModel(
            name='PizzaSize',
        ),
    ]