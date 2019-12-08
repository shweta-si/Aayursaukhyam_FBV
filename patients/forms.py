from django.forms import ModelForm

from .models import *
from django.forms import widgets
from django import forms


# from django.forms.widgets import TextInput, NumberInput

BED_CATEGORY = [('', '--------'), ('SDBed', 'Step_down'), ('NVBed', 'Non_ventilated'), ('VBed', 'Ventilated')]

class HospitalForm(ModelForm):
    registration_code = forms.CharField(widget=forms.TextInput(attrs=
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
    is_ward_type = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                                 {
                                                                                     'class': "form-control form-control-sm"}))
    charges = forms.CharField(widget=forms.NumberInput(attrs=
                                                       {'class': "form-control form-control-sm"}))
    no_of_beds = forms.CharField(widget=forms.NumberInput(attrs=
                                                          {'class': "form-control form-control-sm"}))

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
    wr_type = forms.ModelChoiceField(queryset=WardOrRoomType.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label="")
    building = forms.ModelChoiceField(queryset=Building.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label="")

    class Meta:
        model = Room
        fields = '__all__'


class BedForm(ModelForm):
    bed_no = forms.CharField(widget=forms.TextInput(attrs=
                                                    {'class': "form-control form-control-sm"}))

    bed_type = forms.ChoiceField(choices=BED_CATEGORY, widget=forms.Select(attrs=
                                                                           {'class': "form-control form-control-sm"}))
    room_no = forms.ModelChoiceField(queryset=Room.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label="")
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                           {'class': "form-check form-check-input"}))

    class Meta:
        model = Bed
        fields = '__all__'

    '''def clean_room_no(self):
        room_no = "R"+ self.cleaned_data["room_no"]
        return room_no'''


class WardForm(ModelForm):
    ward_no = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    floor = forms.CharField(widget=forms.TextInput(attrs=
                                                   {'min': 1, 'max': 5, 'type': 'number',
                                                    'class': "form-control form-control-sm"}))
    ward_extension = forms.CharField(widget=forms.NumberInput(attrs=
                                                              {'class': "form-control form-control-sm"}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                           {'class': "form-control"}))
    wr_type = forms.ModelChoiceField(queryset=WardOrRoomType.objects.all(),
                                     widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                     empty_label=None)
    building = forms.ModelChoiceField(queryset=Building.objects.all(),
                                      widget=forms.Select(attrs={'class': "form-control form-control-sm"}),
                                      empty_label=None)

    class Meta:
        model = Ward
        fields = '__all__'

class DepartmentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class': "form-control form-control-sm"}))
    is_healthprof_dept = forms.CharField(widget=forms.CheckboxInput(attrs=
                                                     {'class': "form-control"}))

    class Meta:
        model = Department
        fields = '__all__'

class DesignationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'class': "form-control form-control-sm"}))
    is_healthprof_desg = forms.CharField(widget=forms.CheckboxInput(attrs=
                                                                    {'class': "form-control"}))
    class Meta:
        model = Designation
        fields = '__all__'


#forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))