# Generated by Django 3.0.6 on 2020-06-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Account', '0023_auto_20200618_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharing_post',
            name='BG_Color',
            field=models.CharField(default='rgba(10, 10, 10, .5)', max_length=10),
        ),
        migrations.AlterField(
            model_name='sharing_post',
            name='Font_Color',
            field=models.CharField(default='white', max_length=10),
        ),
    ]