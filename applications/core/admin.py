from django.contrib import admin, messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *


class EmployerCompanyAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','name','iin','description','icon',]
    search_fields = ['user','first_name','last_name','name','iin','description','icon',]

    ordering = ('id',)
    class Meta:
        model = EmployerCompany

class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','branch_land_name', 'city_name', 'company','name','address','link_address','description',]
    search_fields = ['branch_land_name', 'city_name', 'company','name','address','link_address','description',]

    ordering = ('id',)
    class Meta:
        model = Branch

class PositionEmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','employer','name',]
    search_fields = ['name',]

    ordering = ('id',)
    class Meta:
        model = PositionEmployee


class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'id','employer_company','branch','position','salary',
        'time_start',
        ]
    search_fields = [
        'employer_company','branch','position',
        ]

    ordering = ('id',)
    class Meta:
        model = Vacancy


class InvitationAdmin(admin.ModelAdmin):
    list_display = ['id','employer','vacancy','user', 'is_rejected', 'is_accepted']
    search_fields = [
        'employer_company','branch','position',
        ]

    class Meta:
        model = Invitation

    
class LandNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'land_name']
    search_fields = ['land_name',]

    class Meta:
        model = LandName



admin.site.register(LandName,LandNameAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(ReviewBranch)
admin.site.register(PositionEmployee, PositionEmployeeAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(EmployerCompany, EmployerCompanyAdmin)
admin.site.register(Invitation, InvitationAdmin)
