# Generated by Django 3.0.3 on 2020-03-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_auto_20200320_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
