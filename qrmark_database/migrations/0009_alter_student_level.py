# Generated by Django 4.2.2 on 2023-07-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrmark_database', '0008_remove_lecturer_course_remove_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
