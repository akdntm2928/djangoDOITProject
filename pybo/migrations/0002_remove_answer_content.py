# Generated by Django 3.2.8 on 2021-10-27 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='content',
        ),
    ]
