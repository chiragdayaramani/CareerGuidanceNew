# Generated by Django 3.2.8 on 2021-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_after12artscolleges_after12commcolleges'),
    ]

    operations = [
        migrations.AddField(
            model_name='after10colleges',
            name='website',
            field=models.URLField(default='', max_length=500),
        ),
    ]
