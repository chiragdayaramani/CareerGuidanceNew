# Generated by Django 3.2.7 on 2022-02-07 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_result_correct_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='correct_answer',
            new_name='correct_ans',
        ),
    ]
