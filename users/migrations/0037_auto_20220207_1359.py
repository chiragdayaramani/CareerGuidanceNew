# Generated by Django 3.2.7 on 2022-02-07 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_rename_correct_answer_result_correct_ans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='after10',
            old_name='correct_answer',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='result',
            name='correct_ans',
        ),
    ]
