# Generated by Django 3.0.3 on 2020-03-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_food_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='item_image',
            field=models.CharField(max_length=700),
        ),
    ]
