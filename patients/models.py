from django.db import models

from django.core.validators import RegexValidator
from .validators import *  #custom validators ----> validators.py in your app -patient



GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
BLOOD_GROUP_CHOICES = [('Not Known', 'Not Known'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-')]
MODE_OF_PAYMENT_CHOICES = [('Cash', 'Cash'), ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card')]
ROLE_CHOICES = [('Health Professional', 'Health Professional'),('Nurse', 'Nurse'), ('Aaya', 'Aaya'), ('WardBoy', 'WardBoy')]
APPOINTMENT_MODE_CHOICES = [('By Phone', 'By Phone'), ('By Email', 'By Email'), ('By Self', 'By Self')]


# Create your models here.
class Hospital(models.Model):
    reg_code = models.CharField(max_length=16)
    name = models.CharField(max_length=50)
    location = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
                                 message="Phone number must be entered in the format: '99999999999'. Minimum 10 to Maximum 14 digits allowed.")
    contact_no = models.CharField(validators=[phone_regex], max_length=15)
    #photo = models.FileField(upload_to='hospital/pics/')
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #created_by = CreatingUserField(related_name="hospital_created")
    #created_with_session_key = CreatingSessionKeyField()
    #updated_by = LastUserField()
    #updated_with_session_key = LastSessionKeyField()
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
                                 message="Phone number must be entered in the format: '99999999999'. Minimum 10 to Maximum 14 digits allowed.")
    telephone_line1 = models.CharField(validators=[phone_regex], max_length=15)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="hospital_building")

    def __str__(self):
        return self.name


class WardOrRoomType(models.Model):
    wr_type = models.CharField(max_length=20, unique=True)
    # special room 500/-Rs., Semi Private 400/-Rs. Per day
    is_ward_type = models.BooleanField()
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_beds = models.PositiveIntegerField()


    def __str__(self):
        return self.wr_type


class Room(models.Model):
    room_no = models.CharField(max_length=8, unique=True)
    floor = models.PositiveIntegerField()
    room_extension = models.PositiveIntegerField(unique=True, blank=True)
    status = models.BooleanField(default=False)
    wr_type = models.ForeignKey(WardOrRoomType, on_delete=models.CASCADE, related_name="room_type")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="room_building")

    def __str__(self):
        return self.room_no


class Bed(models.Model):
    bed_no = models.CharField(max_length=8, unique=True)
    bed_type = models.CharField(max_length=6)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_bed")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.bed_no


class Ward(models.Model):
    ward_no = models.CharField(max_length=8, unique=True)
    floor = models.PositiveIntegerField()
    ward_extension = models.PositiveIntegerField(unique=True, blank=True)
    status = models.BooleanField(default=False)
    wr_type = models.ForeignKey(WardOrRoomType, blank=True, null=True, on_delete=models.CASCADE,
                                related_name="ward_type")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="ward_building")

    def __str__(self):
        return self.ward_no


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, default=' ')
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP_CHOICES, default='Not Known')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Female')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
                                 message="Phone number must be entered in the format: '99999999999'. Minimum 10 to Maximum 14 digits allowed.")
    telephone_line1 = models.CharField(validators=[phone_regex], max_length=15)
    bed_no = models.ForeignKey(Bed, on_delete=models.CASCADE, related_name="patient_bedno")

    @property
    def full_name(self):
        if self.middle_name == ' ':
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'middle_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Patient, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_name

class Department(models.Model):
    name = models.CharField(max_length=30)
    is_healthprof_dept = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30)
    is_healthprof_desg = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from PIL import Image
from django.conf import settings
class Employee(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP_CHOICES)
    photo = models.ImageField(upload_to='employee/pics/', null=True, blank=True, validators=[validate_image_extension])
    address = models.TextField()
    email_id = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
                                 message="Phone number must be entered in the format: '99999999999'. Minimum 10 to Maximum 14 digits allowed.")
    telephone_line1 = models.CharField(validators=[phone_regex], max_length=15)
    joining_date = models.DateField()
    #bank_account_no = models.CharField(max_length=15)
    #pf_account_no = models.CharField(max_length=15)
    #city = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


    @property
    def get_absolute_image_url(self):
        print("s",self.photo.url)
        return "{0}{1}".format(settings.MEDIA_URL, self.photo.url)

#Creating Thumbnail for our Image -- >Install Pillow
    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

class DeptManager(models.Model):
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Employee_DeptManager_no")
    from_date = models.DateField()
    to_date = models.DateField()
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_no")
    desg_id = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="Designation_DeptManager_name")
    def __str__(self):
        return self.dept_no

# how to calculate health professional pay
class EmployeePayslip(models.Model):
    payment_date = models.DateField()
    print_date = models.DateField()
    pay_days = models.IntegerField()  # working_days - no_of_days
    Income_tax = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    prof_tax = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    pf = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    h_rent = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    da = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    hra = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    other_earning = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    payslip_for_month_of = models.DateTimeField()
    gross_pay = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    total_deduction = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    net_payment = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="emp_no")

    def __str__(self):
        return self.employee_name

    @property
    def full_name(self):
        if self.middle_name == '':
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.full_name


class DrugForm(models.Model):
    # code = models.CharField(max_length=15, null=True, blank=True) #Code
    name = models.CharField(max_length=15, null=True, blank=True)  # Form
    abbreviation = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.abbreviation

    def save(self, *args, **kwargs):
        for field_name in ['abbreviation']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(DrugForm, self).save(*args, **kwargs)


class Dose(models.Model):
    name = models.PositiveIntegerField()  # 500,400
    #abbreviation = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return str(self.name)


class DoseUnit(models.Model):
    name = models.CharField(max_length=6, null=True, blank=True)  # Unit -ml
    drug_form = models.ForeignKey(DrugForm, on_delete=models.CASCADE, related_name="DrugForm_DoseUnit_related")

    def __str__(self):
        return self.name


class MFGCompany(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        for field_name in ['abbreviation']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(MFGCompany, self).save(*args, **kwargs)

class MedicationDosage(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Frequency
    #abbreviation = models.CharField(max_length=15, unique=True)  # Abbreviation

    def __str__(self):
        return self.abbreviation
# Make 1 times before meal --> 1TBM
    @property
    def abbreviation(self):
        line = self.name
        words = line.split()
        letters = [word[0] for word in words]
        return '%s' % ("".join(letters).upper())

class Medicament(models.Model):
    name = models.CharField(max_length=20, unique=True)  # MedicineName 500mg TAB
    mfg_company = models.ForeignKey(MFGCompany, on_delete=models.CASCADE, related_name='MFGCompany_Medicament_related')
    expiry_date = models.DateField()
    batch_id = models.CharField(max_length=12, null=True, blank=True)
    #dosage = models.ForeignKey(MedicationDosage) #Dosage Instructions
    drug_form = models.ForeignKey(DrugForm, on_delete=models.CASCADE, related_name='DrugForm_Medicament_related')
    dose = models.ForeignKey(Dose, on_delete=models.CASCADE, related_name='Dose_Medicament_related')
    dose_unit = models.ForeignKey(DoseUnit, on_delete=models.CASCADE, related_name='DoseUnit_Medicament_related')

    def __str__(self):
        return self.name

    # @property
    # def medicament_name(self):
    #     return "%s %s" % (self.drug_form, self.name)


class Pack(models.Model):  # for tablet box -10 tablet in a strip
    strip_of_tab = models.CharField(max_length=3, unique=True)
    def __str__(self):
        return self.strip_of_tab


class MedicamentPackRate(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='Medicament_MedicamentPackRate_related' )
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='Pack_MedicamentPackRate_related')
    rate = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    def __str__(self):
        return self.id


class MedicamentCharges(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='Medicament_MedicamentCharges_related' )
    qty = models.PositiveIntegerField()
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='Pack_MedicamentCharges_related' )
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    def __str__(self):
        return self.id

class MedicamentBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient_MedicamentBill_related')
    healthprofessional = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Employee_MedicamentBill_related')
    mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
    date = models.DateField()
    medicament = models.ManyToManyField('self', through='MedicamentCharges', symmetrical=False, related_name='Medicament_MedicamentCharges_related' )
    #medicament_charges = models.ManyToManyField(MedicamentCharges, through='MedicamentCharges')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.id

#class MedicamentBillCharges(models.Model):
    #Bill = models.ForeignKey(MedicamentBill)
    #medicament_charges = models.ForeignKey(MedicamentCharges, on_delete=models.CASCADE, related_name='Medicament_bill_charges')
    #medicament_charges = models.ManyToManyField(MedicamentCharges, through='MedicamentBill_related')

    #def __str__(self):
        #return self.id



class Appointment(models.Model):
    appointment_date_taken =models.DateTimeField()
    appointment_mode = models.CharField(max_length=15, choices=APPOINTMENT_MODE_CHOICES, default='By Phone')
    #appointment_date_time = models.DateTimeField()
    #appointment_time = models.TimeField()
    # CATEGORY_APP_TYPE = (('OPD', 'OPD'), ('IPD', 'IPD'))
    # type = models.CharField(max_length=10, choices= CATEGORY_APP_TYPE, default = 'OPD')
    status = models.BooleanField()  # attended or not_attended
    clinical_notes = models.TextField(null=True, blank=True)
    #CATEGORY_URGENCY = (('Normal', 'Normal'), ('Severe', 'Severe'))
    #urgency = models.CharField(max_length=10, choices=CATEGORY_URGENCY, default='Normal')
    healthprofessional = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='HP_Appointment_related')
    #referred_by = models.CharField(max_length=30, blank=True, null=True, default='Self')
    # hospital = models.ForeignKey(Hospital)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient_Appointment_related')

class PatientVisits(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient_PatientVisits_related')
    #date = models.DateField()
    chief_complaints = models.TextField()  # new complaint
    diagnosis = models.TextField()
    blood_pressure = models.CharField(max_length=6, null=True, blank=True, default='80/120')
    weight = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    height = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    advice = models.TextField()
    next_followup = models.DateField(blank=True, null=True)
    # discharged_date = models.DateTimeField(auto_now=True)
    # examined_by = models.ForeignKey(HealthProfessional, related_name='examineddoc')   #patient admitted under doctor
    # reffered_by = models.ForeignKey(ReferredDoctor)
    #prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='Prescription')
    # suffering_from = models.ForeignKey(Disease)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="Appointment_PatientVisits_related")
    # appointment = models.PositiveIntegerField()

    def __str__(self):
        return self.id

class Prescription(models.Model):
    patientvisits = models.ForeignKey(PatientVisits, on_delete=models.CASCADE,
                                      related_name='PatientVisits_Prescription')
    #drug_form = models.ForeignKey(DrugForm, on_delete=models.CASCADE, related_name='Drug')  # Tablet, Capsule
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='Medicament_Prescription_related')
    #medicament = models.ManyToManyField(Medicament, through='Medicament_Prescription')
    medication_dosage = models.ForeignKey(MedicationDosage, on_delete=models.CASCADE, related_name='MedicationDosage_Prescription_related')
    qty = models.IntegerField()
    other_advice = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.id

#class Base(models.Model):
    #m2m = models.ManyToManyField(
        #OtherModel,
        #related_name="%(app_label)s_%(class)s_related",
        #related_query_name="%(app_label)s_%(class)ss",
        #)

#class Meta:
    #abstract = True

#class ChildA(Base):
    #pass

#class ChildB(Base):
    #pass
    #class Meta:
        #verbose_name_plural = "PatientVisits"
        #unique_together = ('id', 'appointment')





#class MedicationDosage(models.Model):
    #code = models.CharField(max_length=15, null=True, blank=True) #Code
    #name = models.CharField(max_length=30, unique=True)  # Frequency
    #abbreviation = models.CharField(max_length=15, unique=True)  # Abbreviation

    #def __str__(self):
        #return self.name








    #     def save(self, * args, ** kwargs):


#          self.appointment_dtls = self.appointment
#          print self.appointment
#
#          return super(PatientVisits, self).save( * args, ** kwargs)









