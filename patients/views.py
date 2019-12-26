from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
#Protecting views ---> decorators @login_required
from django.contrib.auth.decorators import login_required

from .forms import *

#for file upload
from .models import Employee
##helper function used for repetitive pagination code ---which is located in patients app patients/helpers.py
#If helpers.py placed in main project then queryset = helpers.pg_records(request, queryset_list, 10)
from .helpers import pg_records

#from dal import autocomplete    #autocomplete dal


#from .models import *    #autocomplete dal


#class BedAutocomplete(autocomplete.Select2QuerySetView):
    #def get_queryset(self):
        #queryset = Bed.objects.all()
        #if self.q:
            #queryset = queryset.filter(name__istartswith=self.q)
        #return queryset

#Create your views here.
def home(request):
    return render(request,'home.html')
#
#
# def save_all(request, form, tbl_name, page_name, template_name):
#     data = dict()
#     #pg = request.META.get('HTTP_REFERER')  #http://127.0.0.1:8000/hospital/?page=2
#
#     if request.method == 'POST':
#         if form.is_valid():
#             print("success")
#             form.save(commit=True)
#
#             data['form_is_valid'] = True
#             queryset_list = tbl_name.objects.order_by('-id')
#             queryset = pg_records(request, queryset_list, 10)
#             context = {'object_list': queryset}
#             data['data_list'] = render_to_string('patients/' + str(page_name) + '_list_2.html', context)
#         else:
#             print("Failed")
#             data['form_is_valid'] = False
#     context = {'form': form}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)

def save_all(request, form, tbl_name, page_name, template_name):
    data = dict()
    #pg = request.META.get('HTTP_REFERER')  #http://127.0.0.1:8000/hospital/?page=2

    if request.method == 'POST':
        if form.is_valid():
            if(request.FILES == None):
                form.save()             #print("n",request.FILES) < MultiValueDict: {} >
            else:
                form.save(commit=True)  #<MultiValueDict: {'photo': [<InMemoryUploadedFile: ui-icons_777620_256x240.png (image/png)>]}>
                print("n", request.FILES)
            data['form_is_valid'] = True
            queryset_list = tbl_name.objects.order_by('-id')
            queryset = pg_records(request, queryset_list, 10)
            context = {'object_list': queryset}
            data['data_list'] = render_to_string('patients/' + str(page_name) + '_list_2.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def hospital_list(request):
    queryset_list = Hospital.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/hospital_list.html', context)


def hospital_create(request):
    tbl_name = Hospital
    page_name = "hospital"
    if request.method == 'POST':
        form = HospitalForm(request.POST)
    else:
        form = HospitalForm()
    return save_all(request, form, tbl_name, page_name, 'patients/hospital_create.html')


def hospital_update(request, id):
    instance = get_object_or_404(Hospital, id=id)
    tbl_name = Hospital
    page_name = "hospital"
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=instance)
    else:
        form = HospitalForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/hospital_update.html')


def hospital_delete(request, id):
    data = dict()
    instance = get_object_or_404(Hospital, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Hospital.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/hospital_list_2.html', context)
    else:

        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/hospital_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def building_list(request):
    queryset_list = Building.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/building_list.html', context)

@login_required
def building_create(request):
    tbl_name = Building
    page_name = "building"
    if request.method == 'POST':
        form = BuildingForm(request.POST)
    else:
        form = BuildingForm()
    return save_all(request, form, tbl_name, page_name, 'patients/building_create.html')

@login_required
def building_update(request, id):
    instance = get_object_or_404(Building, id=id)
    tbl_name = Building
    page_name = "building"
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=instance)
    else:
        form = BuildingForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/building_update.html')

@login_required
def building_delete(request, id):
    data = dict()
    instance = get_object_or_404(Building, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Building.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/building_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/building_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def wardorroomtype_list(request):
    queryset_list = WardOrRoomType.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/wardorroomtype_list.html', context)

@login_required
def wardorroomtype_create(request):
    tbl_name = WardOrRoomType
    page_name = "wardorroomtype"
    if request.method == 'POST':
        form = WardOrRoomTypeForm(request.POST)
    else:
        form = WardOrRoomTypeForm()
    return save_all(request, form, tbl_name, page_name, 'patients/wardorroomtype_create.html')

@login_required
def wardorroomtype_update(request, id):
    tbl_name = WardOrRoomType
    instance = get_object_or_404(tbl_name, id=id)
    page_name = "wardorroomtype"
    if request.method == 'POST':
        form = WardOrRoomTypeForm(request.POST, instance=instance)
    else:
        form = WardOrRoomTypeForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/wardorroomtype_update.html')

@login_required
def wardorroomtype_delete(request, id):
    data = dict()
    instance = get_object_or_404(WardOrRoomType, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = WardOrRoomType.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/wardorroomtype_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/wardorroomtype_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def room_list(request):
    queryset_list = Room.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/room_list.html', context)

@login_required
def room_create(request):
    tbl_name = Room
    page_name = "room"
    if request.method == 'POST':
        form = RoomForm(request.POST)
    else:
        form = RoomForm()
    return save_all(request, form, tbl_name, page_name, 'patients/room_create.html')

@login_required
def room_update(request, id):
    instance = get_object_or_404(Room, id=id)
    tbl_name = Room
    page_name = "room"
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=instance)
    else:
        form = RoomForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/room_update.html')

@login_required
def room_delete(request, id):
    data = dict()
    instance = get_object_or_404(Room, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Room.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/room_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/room_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def ward_list(request):
    queryset_list = Ward.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/ward_list.html', context)

@login_required
def ward_create(request):
    tbl_name = Ward
    page_name = "ward"
    if request.method == 'POST':
        form = WardForm(request.POST)
    else:
        form = WardForm()
    return save_all(request, form, tbl_name, page_name, 'patients/ward_create.html')

@login_required
def ward_update(request, id):
    instance = get_object_or_404(Ward, id=id)
    tbl_name = Ward
    page_name = "ward"
    if request.method == 'POST':
        form = WardForm(request.POST, instance=instance)
    else:
        form = WardForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/ward_update.html')

@login_required
def ward_delete(request, id):
    data = dict()
    instance = get_object_or_404(Ward, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Ward.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/ward_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/ward_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def bed_list(request):
    queryset_list = Bed.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/bed_list.html', context)

@login_required
def bed_create(request):
    tbl_name = Bed
    page_name = "bed"
    if request.method == 'POST':
        form = BedForm(request.POST)
    else:
        form = BedForm()
    return save_all(request, form, tbl_name, page_name, 'patients/bed_create.html')

@login_required
def bed_update(request, id):
    instance = get_object_or_404(Bed, id=id)
    tbl_name = Bed
    page_name = "bed"
    if request.method == 'POST':
        form = BedForm(request.POST, instance=instance)
    else:
        form = BedForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/bed_update.html')

@login_required
def bed_delete(request, id):
    data = dict()
    instance = get_object_or_404(Bed, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Bed.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/bed_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/bed_delete.html', context, request=request)
    return JsonResponse(data)


def patient_list(request):
    queryset_list = Patient.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/patient_list.html', context)


def patient_create(request):
    tbl_name = Patient
    page_name = "patient"
    if request.method == 'POST':
        form = PatientForm(request.POST)
    else:
        form = PatientForm()
    return save_all(request, form, tbl_name, page_name, 'patients/patient_create.html')


def patient_update(request, id):
    instance = get_object_or_404(Patient, id=id)
    tbl_name = Patient
    page_name = "patient"
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=instance)
    else:
        form = PatientForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/patient_update.html')


def patient_delete(request, id):
    data = dict()
    instance = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Patient.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/patient_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/patient_delete.html', context, request=request)
    return JsonResponse(data)


def department_list(request):
    queryset_list = Department.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/department_list.html', context)


def department_create(request):
    tbl_name = Department
    page_name = "department"
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
    else:
        form = DepartmentForm()
    return save_all(request, form, tbl_name, page_name, 'patients/department_create.html')


def department_update(request, id):
    instance = get_object_or_404(Department, id=id)
    tbl_name = Department
    page_name = "department"
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=instance)
    else:
        form = DepartmentForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/department_update.html')


def department_delete(request, id):
    data = dict()
    instance = get_object_or_404(Department, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Department.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/department_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/department_delete.html', context, request=request)
    return JsonResponse(data)

def designation_list(request):
    queryset_list = Designation.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/designation_list.html', context)


def designation_create(request):
    tbl_name = Designation
    page_name = "designation"
    if request.method == 'POST':
        form = DesignationForm(request.POST)
    else:
        form = DesignationForm()
    return save_all(request, form, tbl_name, page_name, 'patients/designation_create.html')


def designation_update(request, id):
    instance = get_object_or_404(Designation, id=id)
    tbl_name = Designation
    page_name = "designation"
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=instance)
    else:
        form = DesignationForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/designation_update.html')


def designation_delete(request, id):
    data = dict()
    instance = get_object_or_404(Designation, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Designation.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/designation_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/designation_delete.html', context, request=request)
    return JsonResponse(data)


def employee_list(request):
    queryset_list = Employee.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/employee_list.html', context)


def employee_create(request):
    tbl_name = Employee
    page_name = "employee"
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None, request.FILES or None)
    else:
        form = EmployeeForm()
    return save_all(request, form, tbl_name, page_name, 'patients/employee_create.html')


def employee_update(request, id):
    instance = get_object_or_404(Employee, id=id)
    tbl_name = Employee
    page_name = "employee"
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None, request.FILES or None, instance=instance)
    else:
        form = EmployeeForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/employee_update.html')


def employee_delete(request, id):
    data = dict()
    instance = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Employee.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/employee_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/employee_delete.html', context, request=request)
    return JsonResponse(data)


def dept_manager_list(request):
    queryset_list = DeptManager.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/dept_manager_list.html', context)


def dept_manager_create(request):
    tbl_name = DeptManager
    page_name = "dept_manager"
    if request.method == 'POST':
        form = DeptManagerForm(request.POST)
    else:
        form = DeptManagerForm()
    return save_all(request, form, tbl_name, page_name, 'patients/dept_manager_create.html')


def dept_manager_update(request, id):
    instance = get_object_or_404(DeptManager, id=id)
    tbl_name = DeptManager
    page_name = "dept_manager"
    if request.method == 'POST':
        form = DeptManagerForm(request.POST, instance=instance)
    else:
        form = DeptManagerForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/dept_manager_update.html')


def dept_manager_delete(request, id):
    data = dict()
    instance = get_object_or_404(DeptManager, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = DeptManager.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/dept_manager_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/dept_manager_delete.html', context, request=request)
    return JsonResponse(data)


def drug_form_list(request):
    queryset_list = DrugForm.objects.order_by('-id')
    queryset = pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/drug_form_list.html', context)


def drug_form_create(request):
    tbl_name = DrugForm
    page_name = "drug_form"
    if request.method == 'POST':
        form = DrugFormForm(request.POST)
    else:
        form = DrugFormForm()
    return save_all(request, form, tbl_name, page_name, 'patients/drug_form_create.html')


def drug_form_update(request, id):
    instance = get_object_or_404(DrugForm, id=id)
    tbl_name = DrugForm
    page_name = "drug_form"
    if request.method == 'POST':
        form = DrugFormForm(request.POST, instance=instance)
    else:
        form = DrugFormForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/drug_form_update.html')


def drug_form_delete(request, id):
    data = dict()
    instance = get_object_or_404(DrugForm, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = DrugForm.objects.order_by('-id')
        queryset = pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/drug_form_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/drug_form_delete.html', context, request=request)
    return JsonResponse(data)


