# Generated by Django 3.2.8 on 2021-10-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_data',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_data',
            field=models.DateTimeField(null=True),
        ),
    ]
