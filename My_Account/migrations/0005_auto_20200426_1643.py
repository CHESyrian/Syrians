# Generated by Django 3.0.3 on 2020-04-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0004_auto_20200423_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='Cover_Image',
            field=models.ImageField(default='users_profiles/default_images/cover_images/default_cover_image.jpg', upload_to='users_profiles/cover_images'),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Profile_Image',
            field=models.ImageField(default='users_profiles/default_images/default_profile_image.jpg', upload_to='users_profiles/profile_images/'),
        ),
    ]