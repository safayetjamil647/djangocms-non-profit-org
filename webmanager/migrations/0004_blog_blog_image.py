# Generated by Django 3.0.4 on 2020-05-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmanager', '0003_auto_20200519_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
