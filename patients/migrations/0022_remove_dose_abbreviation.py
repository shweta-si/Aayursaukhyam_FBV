# Generated by Django 3.0 on 2020-01-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_employee_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dose',
            name='abbreviation',
        ),
    ]