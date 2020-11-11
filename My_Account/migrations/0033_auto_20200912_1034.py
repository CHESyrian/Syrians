# Generated by Django 3.0.6 on 2020-09-12 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('My_Account', '0032_auto_20200709_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_model',
            name='Codepen_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Facebook_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Github_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Instagram_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Kaggle_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='LinkedIn_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Twitter_Link',
        ),
        migrations.RemoveField(
            model_name='profile_model',
            name='Youtube_Link',
        ),
        migrations.CreateModel(
            name='User_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facebook_Link', models.CharField(default='', max_length=160)),
                ('Twitter_Link', models.CharField(default='', max_length=160)),
                ('Youtube_Link', models.CharField(default='', max_length=160)),
                ('LinkedIn_Link', models.CharField(default='', max_length=160)),
                ('Instagram_Link', models.CharField(default='', max_length=160)),
                ('Github_Link', models.CharField(default='', max_length=160)),
                ('Kaggle_Link', models.CharField(default='', max_length=160)),
                ('Codepen_Link', models.CharField(default='', max_length=160)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]