# Generated by Django 3.1.7 on 2021-02-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='code',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]