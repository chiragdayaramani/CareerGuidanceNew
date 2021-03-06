# Generated by Django 2.2.13 on 2022-03-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220301_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result12scienceCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('count_BCOM', models.CharField(max_length=10)),
                ('count_BAF', models.CharField(max_length=10)),
                ('count_BMS', models.CharField(max_length=10)),
                ('count_CA', models.CharField(default=' ', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='after12science',
            name='correct_answer',
            field=models.CharField(default=' ', max_length=120),
        ),
        migrations.AddField(
            model_name='after12science',
            name='op1',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='after12science',
            name='op2',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='after12science',
            name='op3',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='after12science',
            name='op4',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='after12science',
            name='question_type',
            field=models.CharField(default=' ', max_length=120),
        ),
        migrations.AddField(
            model_name='result12sci',
            name='question_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='after12science',
            name='question',
            field=models.CharField(max_length=900, unique=True),
        ),
        migrations.AlterField(
            model_name='result12sci',
            name='answer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='result12sci',
            name='question',
            field=models.CharField(default='', max_length=255),
        ),
    ]
