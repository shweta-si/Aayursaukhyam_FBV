from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import *
#For Patient date of birth
import datetime
from django import forms

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

#from dal import autocomplete  # for autocomplete



BED_CHOICES = [('', '--------'), ('SDBed', 'Step_down'), ('NVBed', 'Non_ventilated'), ('VBed', 'Ventilated')]
GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
BLOOD_GROUP_CHOICES = [('Not Known', 'Not Known'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-')]
MODE_OF_PAYMENT_CHOICES = [('Cash', 'Cash'), ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card')]
ROLE_CHOICES = [('Health Professional', 'Health Professional'),('Nurse', 'Nurse'), ('Aaya', 'Aaya'), ('WardBoy', 'WardBoy')]
APPOINTMENT_MODE_CHOICES = [('By Phone', 'By Phone'), ('By Email', 'By Email'), ('By Self', 'By Self')]



class HospitalForm(ModelForm):
    reg_code = forms.CharField(widget=forms.TextInput(attrs=
                                                               {'class': "form-control form-control-sm"}))
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    location = forms.CharField(widget=forms.Textarea(attrs=
                                                     {'rows': "1", 'cols': "25",
                                                      'class': "form-control form-control-sm"}), required=False)
    contact_no = forms.CharField(widget=forms.TextInput(attrs=
                                                        {'class': "form-control form-control-sm"}))

    class Meta:
        model = Hospital
        fields = '__all__'


class BuildingForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    location = forms.CharField(widget=forms.Textarea(attrs=
                                                     {'rows': "1", 'cols': "25",
                                                      'class': "form-control form-control-sm"}),
                               required=False)
    telephone_line1 = forms.CharField(widget=forms.TextInput(attrs=
                                                             {'class': "form-control form-control-sm"}))
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label="")

    class Meta:
        model = Building
        fields = '__all__'


class WardOrRoomTypeForm(ModelForm):
    wr_type = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    is_ward_type = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'class': "form-control form-control-sm"}))
    charges = forms.CharField(widget=forms.NumberInput(attrs=
                                        {'class': "form-control form-control-sm"}))
    no_of_beds = forms.CharField(widget=forms.NumberInput(attrs={'class': "form-control form-control-sm"}))

    class Meta:
        model = WardOrRoomType
        fields = '__all__'


class RoomForm(ModelForm):
    room_no = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    floor = forms.CharField(widget=forms.TextInput(attrs=
                                                       {'min': 1, 'max': 5, 'type': 'number',
                                                        'class': "form-control form-control-sm"}))
    room_extension = forms.CharField(widget=forms.NumberInput(attrs=
                                                        {'class': "form-control form-control-sm"}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                        {'class': "form-control form-control-sm"}))
    wr_type = forms.ModelChoiceField(queryset=WardOrRoomType.objects.filter(is_ward_type='False'),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label="")
    building = forms.ModelChoiceField(queryset=Building.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label="")

    class Meta:
        model = Room
        fields = '__all__'

class WardForm(ModelForm):
    ward_no = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    floor = forms.CharField(widget=forms.TextInput(attrs=
                                                   {'min': 1, 'max': 5, 'type': 'number',
                                                    'class': "form-control form-control-sm"}))
    ward_extension = forms.CharField(widget=forms.NumberInput(attrs=
                                                              {'class': "form-control form-control-sm"}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                           {'class': "form-check form-check-input"}))
    wr_type = forms.ModelChoiceField(queryset=WardOrRoomType.objects.filter(is_ward_type='True'),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    building = forms.ModelChoiceField(queryset=Building.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label=None)

    class Meta:
        model = Ward
        fields = '__all__'

class BedForm(ModelForm):
    bed_no = forms.CharField(widget=forms.TextInput(attrs=
                                                    {'class': "form-control form-control-sm"}))

    bed_type = forms.ChoiceField(choices=BED_CHOICES, widget=forms.Select(attrs=
                                                                           {'class': "form-control form-control-sm"}))
    room_no = forms.ModelChoiceField(queryset=Room.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label="")
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                           {'class': "form-check form-check-input"}))

    class Meta:
        model = Bed
        exclude =['status']
        #fields = '__all__'

    '''def clean_room_no(self):
        room_no = "R"+ self.cleaned_data["room_no"]
        return room_no'''

class PatientForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs=
                                                    {'class': "form-control form-control-sm",
                                                     'placeholder': 'First Name'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs=
                                                        {'class': "form-control form-control-sm",
                                                         'placeholder': 'Middle Name',
                                                        }), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs=
                                                        {'class': "form-control form-control-sm",
                                                         'placeholder': 'Last Name'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

                                 #input_formats=['%d/%m/%Y'],
                                #widget=forms.DateTimeInput(attrs={
                                                #'class': 'form-control datetimepicker-input',
                                                #'id' : "id_date_of_birth",
                                                #'data-toggle' : "datetimepicker",
                                                #'data-target' : "#datetimepicker1"
                                                 #})
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    telephone_line1 = forms.CharField(widget=forms.TextInput(attrs=
                                                        {'class': "form-control form-control-sm"}))
    bed_no = forms.ModelChoiceField(queryset=Bed.objects.all(),
                                    widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                    empty_label=None)


    #django autocomplete

    #bed_no = forms.ModelChoiceField(queryset=Bed.objects.all(),
                           #widget=autocomplete.ModelSelect2(url='bed-autocomplete'))
    class Meta:
        model = Patient
        fields = '__all__'

# Patient Birth date cannot be in the future -- set DateField to only accept Today & past dates
    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        date_of_birth = cleaned_data['date_of_birth']

        if date_of_birth > datetime.date.today():
            raise forms.ValidationError("The birth date of patient cannot be in the future!")
        return cleaned_data



class DepartmentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    is_healthprof_dept = forms.CharField(required=False, widget=forms.CheckboxInput(attrs=
                                                     {'class': "form-check form-check-input"}))

    class Meta:
        model = Department
        fields = '__all__'

class DesignationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    is_healthprof_desg = forms.CharField(widget=forms.CheckboxInput(attrs=
                                                                    {'class': "form-control"}), required=False)
    class Meta:
        model = Designation
        fields = '__all__'


class EmployeeForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs=
                                                             {'class': "form-control form-control-sm"}))
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs=
                                                  {'class' : "form-control form-control-sm"}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'type': 'file'}))
    address = forms.CharField(widget=forms.Textarea(attrs=
                                          {'rows': "1", 'cols': "25",
                                           'class': "form-control form-control-sm"}), required=False)
    email_id = forms.EmailField(widget=forms.EmailInput())
    telephone_line1 = forms.CharField(widget=forms.TextInput(attrs=
                                                      {'class': "form-control form-control-sm"}))
    joining_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs=
                                                  {'class' : "form-control form-control-sm"}))

    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, *kwargs)
        self.fields['photo'].required = False

class DeptManagerForm(ModelForm):
    dept_no = forms.ModelChoiceField(queryset=Department.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label=None)
    from_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    emp_no = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                    widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                    empty_label=None)
    desg_id = forms.ModelChoiceField(queryset= Designation.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)

    class Meta:
        model = DeptManager
        fields = '__all__'


class DrugFormForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    abbreviation =  forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    class Meta:
        model = DrugForm
        fields = '__all__'


class DoseForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    abbreviation = forms.CharField(widget=forms.TextInput(attrs=
                                                          {'class': "form-control form-control-sm"}))

    class Meta:
        model = Dose
        fields = '__all__'

class DoseUnitForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    drug_form = forms.ModelChoiceField(queryset= DrugForm.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)

    class Meta:
        model = DoseUnit
        fields = '__all__'

class MFGCompanyForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    abbreviation = forms.CharField(widget=forms.TextInput(attrs=
                                                          {'class': "form-control form-control-sm"}))

    class Meta:
        model = MFGCompany
        fields = '__all__'

class MedicationDosageForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    abbreviation = forms.CharField(widget=forms.TextInput(attrs=
                                                          {'class': "form-control form-control-sm"}))

    class Meta:
        model = MedicationDosage
        fields = '__all__'

class MedicamentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    mfg_company = forms.CharField(widget=forms.TextInput(attrs=
                                                          {'class': "form-control form-control-sm"}))
    expiry_date = forms.DateField(widget=forms.DateInput())
    batch_id = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    drug_form = forms.ModelChoiceField(queryset= DrugForm.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    dose = forms.ModelChoiceField(queryset= Dose.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    dose_unit = forms.ModelChoiceField(queryset= DoseUnit.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    class Meta:
        model = Medicament
        fields = '__all__'

class PackForm(ModelForm):
    strip_of_tab = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))

    class Meta:
        model = Pack
        fields = '__all__'

class MedicamentPackRateForm(ModelForm):
    medicament = forms.ModelChoiceField(queryset= Medicament.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    pack =  forms.ModelChoiceField(queryset= Pack.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    rate = forms.DecimalField()

    class Meta:
        model = MedicamentPackRate
        fields = '__all__'

class MedicamentChargesForm(ModelForm):
    medicament = forms.ModelChoiceField(queryset= Medicament.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    qty = forms.NumberInput(attrs={'size': 5 })
    pack = forms.ModelChoiceField(queryset=Pack.objects.all(),
                                  widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                  empty_label=None)
    amount = forms.DecimalField()
    class Meta:
        model = MedicamentCharges
        exclude = ['amount']

class MedicamentBillForm(ModelForm):
    patient  =forms.ModelChoiceField(queryset= Medicament.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    healthprofessional = forms.ModelChoiceField(queryset= Medicament.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    mode_of_payment = forms.ChoiceField(choices=MODE_OF_PAYMENT_CHOICES, widget=forms.Select(attrs=
                                                  {'class' : "form-control form-control-sm"}))
    date = forms.DateInput()

    class Meta:
        model = MedicamentCharges
        exclude = ['medicament_charges', 'total']


class AppointmentForm(ModelForm):
    appointment_date_taken  = forms.DateTimeInput()

    appointment_mode = forms.ChoiceField(choices=APPOINTMENT_MODE_CHOICES, widget=forms.Select(attrs=
                                               {'class': "form-control form-control-sm"}))
    clinical_notes = forms.CharField(widget=forms.Textarea(attrs=
                                                     {'rows': "1", 'cols': "25",
                                                      'class': "form-control form-control-sm"}), required=False)
    healthprofessional = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                                widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                                empty_label=None)
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(),
                                                widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                                empty_label=None)

    class Meta:
        model = Appointment
        exclude = ['status']


class PatientVisitsForm(ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(),
                                        widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                        empty_label=None)
    chief_complaints = forms.CharField(widget=forms.Textarea(attrs=
                                             {'rows': "1", 'cols': "25",
                                            'class': "form-control form-control-sm"}), required=False)
    diagnosis = forms.CharField(widget=forms.Textarea(attrs=
                                             {'rows': "1", 'cols': "25",
                                            'class': "form-control form-control-sm"}), required=False)
    blood_pressure = forms.CharField(widget=forms.TextInput(attrs=
                                            {'class': "form-control form-control-sm"}))
    weight = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    height = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    advice = forms.CharField(widget=forms.Textarea(attrs={'cols': "25", 'rows': "1", }), required=False)
    next_followup = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    appointment = forms.ModelChoiceField(queryset=Appointment.objects.all(), widget=forms.HiddenInput())

PrescriptionFormSet = inlineformset_factory(
    PatientVisits, Prescription, extra=1,
    fields=('medicament', 'medication_dosage','qty', 'other_advice'),
    #widgets={'drug_form': forms.widgets.ChoiceWidget('DrugForm'),
             #'medicament': forms.widgets.ChoiceWidget('Medicament'),
             #'medication_dosage': forms.widgets.ChoiceWidget('MedicationDosage'),
             #'qty': forms.NumberInput(attrs={'size': 5, })},
    can_delete=True)
