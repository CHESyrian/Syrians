# Generated by Django 3.0.6 on 2020-06-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0015_auto_20200609_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_model',
            name='Followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile_model',
            name='Friends',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sharing_image',
            name='Likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sharing_image',
            name='Loves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sharing_image',
            name='Shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Cover_Image',
            field=models.ImageField(default='users_profiles/covers_images/default_cover_image.jpg', upload_to='users_profiles/covers_images/'),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Profile_Image',
            field=models.ImageField(default='users_profiles/profiles_images/default_profile_image.jpg', upload_to='users_profiles/profiles_images/'),
        ),
    ]
