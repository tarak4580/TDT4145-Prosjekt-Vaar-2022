# Generated by Django 4.0.2 on 2022-02-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupUp', '0002_remove_group_image_alter_group_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
