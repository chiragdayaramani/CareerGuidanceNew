# Generated by Django 3.2.7 on 2022-02-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_after10_result_result10count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='answer',
            field=models.CharField(default='', max_length=900),
        ),
    ]
