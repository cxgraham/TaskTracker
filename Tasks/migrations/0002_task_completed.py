# Generated by Django 2.2.4 on 2022-12-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
