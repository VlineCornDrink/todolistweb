# Generated by Django 5.0.4 on 2024-04-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_remove_task_completed_remove_task_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
