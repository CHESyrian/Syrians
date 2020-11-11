# Generated by Django 3.0.6 on 2020-06-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0019_auto_20200615_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharing_post',
            name='Shares',
        ),
        migrations.AddField(
            model_name='sharing_post',
            name='BG_Color',
            field=models.CharField(default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='sharing_post',
            name='Font_Color',
            field=models.CharField(default='black', max_length=10),
        ),
        migrations.AddField(
            model_name='sharing_post',
            name='Font_Size',
            field=models.IntegerField(default=18),
        ),
    ]