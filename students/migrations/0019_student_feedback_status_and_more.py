# Generated by Django 5.0.3 on 2024-04-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_alter_student_feedback_feedback_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student_feedback',
            name='feedback_reply',
            field=models.TextField(default='', null=True),
        ),
    ]