# Generated by Django 3.2.2 on 2021-05-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-09-12'),
            preserve_default=False,
        ),
    ]
