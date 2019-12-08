from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .forms import *
# helper used here for repetitative pagination code
from Aayursaukhyam import helpers

#Create your views here.
def home(request):
    return render(request,'home.html')


def save_all(request, form, tbl_name, page_name, template_name):
    data = dict()
    #pg = request.META.get('HTTP_REFERER')  #http://127.0.0.1:8000/hospital/?page=2

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            queryset_list = tbl_name.objects.order_by('-id')
            queryset = helpers.pg_records(request, queryset_list, 10)
            context = {'object_list': queryset}
            data['data_list'] = render_to_string('patients/' + str(page_name) + '_list_2.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def hospital_list(request):
    queryset_list = Hospital.objects.order_by('-id')
    queryset = helpers.pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/hospital_list.html', context)

@login_required
def hospital_create(request):
    tbl_name = Hospital
    page_name = "hospital"
    if request.method == 'POST':
        form = HospitalForm(request.POST)
    else:
        form = HospitalForm()
    return save_all(request, form, tbl_name, page_name, 'patients/hospital_create.html')

@login_required
def hospital_update(request, id):
    instance = get_object_or_404(Hospital, id=id)
    tbl_name = Hospital
    page_name = "hospital"
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=instance)
    else:
        form = HospitalForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/hospital_update.html')

@login_required
def hospital_delete(request, id):
    data = dict()
    instance = get_object_or_404(Hospital, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Hospital.objects.order_by('-id')
        queryset = helpers.pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/hospital_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/hospital_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def building_list(request):
    queryset_list = Building.objects.order_by('-id')
    queryset = helpers.pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/building_list.html', context)

@login_required(login_url = 'login')
def building_create(request):
    tbl_name = Building
    page_name = "building"
    if request.method == 'POST':
        form = BuildingForm(request.POST)
    else:
        form = BuildingForm()
    return save_all(request, form, tbl_name, page_name, 'patients/building_create.html')

@login_required(login_url = 'login')
def building_update(request, id):
    instance = get_object_or_404(Building, id=id)
    tbl_name = Building
    page_name = "building"
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=instance)
    else:
        form = BuildingForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/building_update.html')

@login_required(login_url = 'login')
def building_delete(request, id):
    data = dict()
    instance = get_object_or_404(Building, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = Building.objects.order_by('-id')
        queryset = helpers.pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/building_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/building_delete.html', context, request=request)
    return JsonResponse(data)

@login_required(login_url = 'login')
def wardorroomtype_list(request):
    queryset_list = WardOrRoomType.objects.order_by('-id')
    queryset = helpers.pg_records(request, queryset_list, 10)
    context = {'object_list': queryset}
    return render(request, 'patients/wardorroomtype_list.html', context)

@login_required(login_url = 'login')
def wardorroomtype_create(request):
    tbl_name = WardOrRoomType
    page_name = "wardorroomtype"
    if request.method == 'POST':
        form = WardOrRoomTypeForm(request.POST)
    else:
        form = WardOrRoomTypeForm()
    return save_all(request, form, tbl_name, page_name, 'patients/wardorroomtype_create.html')

@login_required(login_url = 'login')
def wardorroomtype_update(request, id):
    tbl_name = WardOrRoomType
    instance = get_object_or_404(tbl_name, id=id)
    page_name = "wardorroomtype"
    if request.method == 'POST':
        form = WardOrRoomTypeForm(request.POST, instance=instance)
    else:
        form = WardOrRoomTypeForm(instance=instance)
    return save_all(request, form, tbl_name, page_name, 'patients/wardorroomtype_update.html')

@login_required(login_url = 'login')
def wardorroomtype_delete(request, id):
    data = dict()
    instance = get_object_or_404(WardOrRoomType, id=id)
    if request.method == "POST":
        instance.delete()
        data['form_is_valid'] = True
        queryset_list = WardOrRoomType.objects.order_by('-id')
        queryset = helpers.pg_records(request, queryset_list, 10)
        context = {'object_list': queryset}
        data['data_list'] = render_to_string('patients/wardorroomtype_list_2.html', context)
    else:
        context = {'instance': instance}
        data['html_form'] = render_to_string('patients/wardorroomtype_delete.html', context, request=request)
    return JsonResponse(data)




