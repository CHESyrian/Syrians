# Generated by Django 3.0.6 on 2020-07-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0028_auto_20200708_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='Codepen_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Facebook_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Github_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Instagram_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Kaggle_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='LinkedIn_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Twitter_Link',
            field=models.CharField(default=None, max_length=160),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='Youtube_Link',
            field=models.CharField(default=None, max_length=160),
        ),
    ]
