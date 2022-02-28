# Generated by Django 3.2.8 on 2021-10-14 15:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_after12medicolleges'),
    ]

    operations = [
        migrations.CreateModel(
            name='After12artscolleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(default='', max_length=1000)),
                ('college_address', models.CharField(default='', max_length=1000)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='After12commcolleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(default='', max_length=1000)),
                ('college_address', models.CharField(default='', max_length=1000)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None)),
            ],
        ),
    ]
