# Generated by Django 4.2.2 on 2023-08-28 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrmark_database', '0021_alter_attendance_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniquecode',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='uniquecode',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='uniquecode',
            name='valid_date',
        ),
    ]