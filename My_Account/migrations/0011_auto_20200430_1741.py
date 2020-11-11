# Generated by Django 3.0.3 on 2020-04-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0010_auto_20200430_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharing_image',
            name='Upload_Path',
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Cover_Image',
            field=models.ImageField(default='default_images/default_cover_image.jpg', upload_to='users_profiles/cover_images/'),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Profile_Image',
            field=models.ImageField(default='default_images/default_profile_image.jpg', upload_to='users_profiles/profile_images/'),
        ),
        migrations.AlterField(
            model_name='sharing_image',
            name='Image',
            field=models.ImageField(upload_to='users_profiles/uploads_images/'),
        ),
    ]
