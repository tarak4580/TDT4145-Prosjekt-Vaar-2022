# Generated by Django 4.0.2 on 2022-02-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupUp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.FileField(blank=True, upload_to='images/', verbose_name=''),
        ),
    ]