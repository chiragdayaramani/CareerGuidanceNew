# Generated by Django 3.2.8 on 2021-10-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_after10colleges_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='after12artscolleges',
            name='website',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='after12commcolleges',
            name='website',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='after12engcolleges',
            name='website',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='after12medicolleges',
            name='website',
            field=models.URLField(default='', max_length=500),
        ),
    ]
