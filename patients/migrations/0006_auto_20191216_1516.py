# Generated by Django 3.0 on 2019-12-16 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20191213_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doseunit',
            old_name='drugform',
            new_name='drug_form',
        ),
        migrations.RenameField(
            model_name='medicament',
            old_name='doseunit',
            new_name='dose_unit',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_date_time',
        ),
        migrations.AddField(
            model_name='deptmanager',
            name='emp_no',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='employee_no', to='patients.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicamentbill',
            name='medicament',
            field=models.ManyToManyField(related_name='Medicament_MedicamentCharges_related', through='patients.MedicamentCharges', to='patients.MedicamentBill'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medication_dosage',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='MedicationDosage_Prescription_related', to='patients.MedicationDosage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.DeleteModel(
            name='MedicamentBillCharges',
        ),
    ]
