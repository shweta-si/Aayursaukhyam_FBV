# Generated by Django 3.0 on 2020-01-07 17:17

from django.db import migrations, models
import patients.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_remove_dose_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee/pics/', validators=[patients.validators.validate_image_extension]),
        ),
    ]