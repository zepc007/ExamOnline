# Generated by Django 3.0.3 on 2020-04-25 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_student_clazz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='clazz',
        ),
        migrations.AlterModelTable(
            name='clazz',
            table='user_class',
        ),
    ]
