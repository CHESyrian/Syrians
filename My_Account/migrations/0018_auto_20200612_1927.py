# Generated by Django 3.0.6 on 2020-06-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0017_auto_20200612_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharing_image',
            old_name='Likes',
            new_name='Amazing_Num',
        ),
        migrations.RenameField(
            model_name='sharing_image',
            old_name='Loves',
            new_name='Good_Num',
        ),
        migrations.RenameField(
            model_name='sharing_post',
            old_name='Likes',
            new_name='Amazing_Num',
        ),
        migrations.RenameField(
            model_name='sharing_post',
            old_name='Loves',
            new_name='Good_Num',
        ),
    ]
