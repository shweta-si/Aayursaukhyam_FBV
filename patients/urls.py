from django.urls import path, re_path

from . import views
from dal import autocomplete
urlpatterns = [
    path('', views.home, name='home'),

    #for dal autocomplete
    #re_path(r'^bed-autocomplete/$', BedAutocomplete.as_view(), name='bed-autocomplete'),

    re_path(r'^hospital/$', views.hospital_list, name='hospital_list'),
    re_path(r'^hospital/create$', views.hospital_create, name='hospital_create'),
    re_path(r'^hospital/(?P<id>\d+)/update$', views.hospital_update, name='hospital_update'),
    re_path(r'^hospital/(?P<id>\d+)/delete$', views.hospital_delete, name='hospital_delete'),

    re_path(r'^building/$', views.building_list, name='building_list'),
    re_path(r'^building/create$', views.building_create, name='building_create'),
    re_path(r'^building/(?P<id>\d+)/update$', views.building_update, name='building_update'),
    re_path(r'^building/(?P<id>\d+)/delete$', views.building_delete, name='building_delete'),

    re_path(r'^wardorroomtype/$', views.wardorroomtype_list, name='wardorroomtype_list'),
    re_path(r'^wardorroomtype/create$', views.wardorroomtype_create, name='wardorroomtype_create'),
    re_path(r'^wardorroomtype/(?P<id>\d+)/update$', views.wardorroomtype_update, name='wardorroomtype_update'),
    re_path(r'^wardorroomtype/(?P<id>\d+)/delete$', views.wardorroomtype_delete, name='wardorroomtype_delete'),

    re_path(r'^room/$', views.room_list, name='room_list'),
    re_path(r'^room/create$', views.room_create, name='room_create'),
    re_path(r'^room/(?P<id>\d+)/update$', views.room_update, name='room_update'),
    re_path(r'^room/(?P<id>\d+)/delete$', views.room_delete, name='room_delete'),

    re_path(r'^ward/$', views.ward_list, name='ward_list'),
    re_path(r'^ward/create$', views.ward_create, name='ward_create'),
    re_path(r'^ward/(?P<id>\d+)/update$', views.ward_update, name='ward_update'),
    re_path(r'^ward/(?P<id>\d+)/delete$', views.ward_delete, name='ward_delete'),

    re_path(r'^bed/$', views.bed_list, name='bed_list'),
    re_path(r'^bed/create$', views.bed_create, name='bed_create'),
    re_path(r'^bed/(?P<id>\d+)/update$', views.bed_update, name='bed_update'),
    re_path(r'^bed/(?P<id>\d+)/delete$', views.bed_delete, name='bed_delete'),

    re_path(r'^patient/$', views.patient_list, name='patient_list'),
    re_path(r'^patient/create$', views.patient_create, name='patient_create'),
    re_path(r'^patient/(?P<id>\d+)/update$', views.patient_update, name='patient_update'),
    re_path(r'^patient/(?P<id>\d+)/delete$', views.patient_delete, name='patient_delete'),

    re_path(r'^department/$', views.department_list, name='department_list'),
    re_path(r'^department/create$', views.department_create, name='department_create'),
    re_path(r'^department/(?P<id>\d+)/update$', views.department_update, name='department_update'),
    re_path(r'^department/(?P<id>\d+)/delete$', views.department_delete, name='department_delete'),

    re_path(r'^designation/$', views.designation_list, name='designation_list'),
    re_path(r'^designation/create$', views.designation_create, name='designation_create'),
    re_path(r'^designation/(?P<id>\d+)/update$', views.designation_update, name='designation_update'),
    re_path(r'^designation/(?P<id>\d+)/delete$', views.designation_delete, name='designation_delete'),

    re_path(r'^employee/$', views.employee_list, name='employee_list'),
    re_path(r'^employee/create$', views.employee_create, name='employee_create'),
    re_path(r'^employee/(?P<id>.*)/update$', views.employee_update, name='employee_update'),
    re_path(r'^employee/(?P<id>\d+)/delete$', views.employee_delete, name='employee_delete'),

    re_path(r'^dept_manager/$', views.dept_manager_list, name='dept_manager_list'),
    re_path(r'^dept_manager/create$', views.dept_manager_create, name='dept_manager_create'),
    re_path(r'^dept_manager/(?P<id>\d+)/update$', views.dept_manager_update, name='dept_manager_update'),
    re_path(r'^dept_manager/(?P<id>\d+)/delete$', views.dept_manager_delete, name='dept_manager_delete'),

    re_path(r'^drug_form/$', views.drug_form_list, name='drug_form_list'),
    re_path(r'^drug_form/create$', views.drug_form_create, name='drug_form_create'),
    re_path(r'^drug_form/(?P<id>\d+)/update$', views.drug_form_update, name='drug_form_update'),
    re_path(r'^drug_form/(?P<id>\d+)/delete$', views.drug_form_delete, name='drug_form_delete'),

    re_path(r'^dose/$', views.dose_list, name='dose_list'),
    re_path(r'^dose/create$', views.dose_create, name='dose_create'),
    re_path(r'^dose/(?P<id>\d+)/update$', views.dose_update, name='dose_update'),
    re_path(r'^dose/(?P<id>\d+)/delete$', views.dose_delete, name='dose_delete'),

    re_path(r'^dose_unit/$', views.dose_unit_list, name='dose_unit_list'),
    re_path(r'^dose_unit/create$', views.dose_unit_create, name='dose_unit_create'),
    re_path(r'^dose_unit/(?P<id>\d+)/update$', views.dose_unit_update, name='dose_unit_update'),
    re_path(r'^dose_unit/(?P<id>\d+)/delete$', views.dose_unit_delete, name='dose_unit_delete'),

    re_path(r'^mfg_company/$', views.mfg_company_list, name='mfg_company_list'),
    re_path(r'^mfg_company/create$', views.mfg_company_create, name='mfg_company_create'),
    re_path(r'^mfg_company/(?P<id>\d+)/update$', views.mfg_company_update, name='mfg_company_update'),
    re_path(r'^mfg_company/(?P<id>\d+)/delete$', views.mfg_company_delete, name='mfg_company_delete'),

    re_path(r'^medication_dosage/$', views.medication_dosage_list, name='medication_dosage_list'),
    re_path(r'^medication_dosage/create$', views.medication_dosage_create, name='medication_dosage_create'),
    re_path(r'^medication_dosage/(?P<id>\d+)/update$', views.medication_dosage_update, name='medication_dosage_update'),
    re_path(r'^medication_dosage/(?P<id>\d+)/delete$', views.medication_dosage_delete, name='medication_dosage_delete'),
    re_path(r'^get-dose-unit/', views.get_dose_unit, name='get_dose_unit'),
    re_path(r'^medicament/$', views.medicament_list, name='medicament_list'),
    re_path(r'^medicament/create$', views.medicament_create, name='medicament_create'),
    re_path(r'^medicament/(?P<id>\d+)/update$', views.medicament_update, name='medicament_update'),
    re_path(r'^medicament/(?P<id>\d+)/delete$', views.medicament_delete, name='medicament_delete'),
]
