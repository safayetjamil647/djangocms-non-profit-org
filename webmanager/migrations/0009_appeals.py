# Generated by Django 3.0.4 on 2020-05-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmanager', '0008_auto_20200521_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeals_title', models.CharField(max_length=100)),
                ('appeals_desc', models.TextField(max_length=1000)),
                ('appeals_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
