# Generated by Django 3.0 on 2019-12-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20191222_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='employee/pics/'),
        ),
    ]
