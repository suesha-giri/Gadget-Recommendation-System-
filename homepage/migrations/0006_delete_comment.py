# Generated by Django 3.1.4 on 2021-05-20 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20210519_1728'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]