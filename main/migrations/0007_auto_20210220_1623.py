# Generated by Django 3.1.7 on 2021-02-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210220_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='lecture_days',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='class',
            name='office_days',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='class',
            name='recitation_days',
            field=models.CharField(max_length=30),
        ),
    ]
