# Generated by Django 3.0.6 on 2020-06-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0021_remove_sharing_image_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharing_image',
            name='Stars_Num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sharing_post',
            name='Stars_Num',
            field=models.IntegerField(default=0),
        ),
    ]
