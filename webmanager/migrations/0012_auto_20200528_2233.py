# Generated by Django 3.0.4 on 2020-05-28 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmanager', '0011_auto_20200527_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appeal',
            old_name='appeals_desc',
            new_name='appeal_desc',
        ),
        migrations.RenameField(
            model_name='appeal',
            old_name='appeals_pic',
            new_name='appeal_pic',
        ),
        migrations.RenameField(
            model_name='appeal',
            old_name='appeals_title',
            new_name='appeal_title',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='sponsors_desc',
            new_name='sponsor_desc',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='sponsors_pic',
            new_name='sponsor_pic',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='sponsors_title',
            new_name='sponsor_title',
        ),
    ]
