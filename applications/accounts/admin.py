from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _



@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'verification_code','is_verified_email', 'password', 'is_delete',)}),
        (_('Permissions'), {'fields': ('role','is_staff', 'is_active', 'is_superuser','user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
            )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1','password2', 'is_delete', 'is_active', 'is_superuser', ),
        }),
    )
    list_display = ['id','email','verification_code', 'phone',  'is_staff', 'is_delete', 'is_active','role', 'is_superuser', ]
    search_fields = ['email', 'phone',  ]
    list_editable = ['is_staff', 'is_delete', 'is_active','role',  'is_superuser',]
    ordering = ('id',)
    filter_horizontal = ('groups', 'user_permissions')

    class Meta:
        model = User


def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["code", "country", "ip", "url", "count"])
    for s in queryset:
        writer.writerow([s.code, s.country, s.ip, s.url, s.count])



class UniversityInline(admin.StackedInline):  
    model = University
    extra = 1


class PassportAndTermInline(admin.StackedInline):  
    model = PassportAndTerm
    extra = 1


class PaymentAdmin(admin.StackedInline): 
    model = Payment
    extra = 1


class Deal(admin.StackedInline):
    model = Deal
    extra = 1


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id', 'user', 'first_name', 'last_name', 'nationality_ru',
        'german', 'english', 'russian',
    )

    search_fields = ('user', 'nationality_ru', 'gender_ru', 'english', 'russian', 'german',)
    list_filter = ('gender_ru', 'nationality_ru', 'english', 'russian', 'german',)
    fieldsets = (
        (None, {'fields': (
            'user', 'first_name', 'first_name_ru','first_name_de', 'last_name', 'last_name_ru','last_name_de',
            'middle_name', 'middle_name_ru','middle_name_de', 'profile_photo',
            'gender_ru', 'gender_en', 'gender_de',
            'nationality_ru', 'nationality_en', 'nationality_de',
            'birth_country_ru', 'birth_country_en', 'birth_country_de',
            'birth_region_ru', 'birth_region_en', 'birth_region_de',
            'date_of_birth', 'phone', 'whatsapp_phone_number',
            'german', 'english', 'russian',
        )}),
    )

    inlines = [
        UniversityInline, PassportAndTermInline, 
        PaymentAdmin, Deal,
        ]  
    
    # actions = [download_csv]






@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'value_rating', 'rating_date', 'employer',)
    search_fields = ('user__email', 'value_rating', 'employer',)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('employer', 'user', 'text', 'creation_date')
    search_fields = ('user__email', 'text')




@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_company', 'company', 'position', 'start_date', 'country',)
    search_fields = ('user__email', 'company', 'position', 'country',)
    list_filter = ('type_company', 'position', 'country',)


    fieldsets = (
        (None, {'fields': ('user', )}),
        ('Details', {'fields': ('company', 'type_company', 'position',)}),
        ('Worktime', {'fields': ('start_date', 'end_date',)}),
        ('Important dates', {'fields': ('responsibilities', 'country',)}),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'debt', 'payment_date', 'payment_accepted',)
    search_fields = ('user__email',)
    list_filter = ('payment_accepted', 'payment_date',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Payment Details', {'fields': ('total_amount', 'total_amount_in_words', 'initial_fee', 'initial_fee_in_words', 'average_fee', 'average_fee_in_words', 'final_fee', 'final_fee_in_words', 'debt', 'debt_in_words', 'payment_date',)}),
        ('Payment Acceptance', {'fields': ('payment_accepted_by', 'payment_accepted_date', 'payment_accepted',)}),
    )

# from django.http import HttpResponse
# import os
# from docx import Document
# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from django.urls import path
# from django.urls import reverse_lazy
# import zipfile

# class ContractAdmin(admin.ModelAdmin):
#     list_display = ('title', 'first_name', 'last_name', 'download_contract',)
#     search_fields = ('title', 'first_name', 'last_name',)

#     def download_contract(self, obj):
#         return '<a href="{}">Download Word</a>'.format(reverse_lazy('admin:download_contract', args=[obj.pk]))
#     download_contract.allow_tags = True
#     download_contract.short_description = _('Download Word')

#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('download_contract/<int:pk>/', self.download_contract_view, name='download_contract'),
#         ]
#         return my_urls + urls

#     def download_contract_view(self, request, pk):
#         contract = self.get_object(request, pk=pk)
#         if contract:
#             # Создание нового документа Word
#             document = Document()
#             # Добавление данных о контракте в документ
#             document.add_heading('Contract', level=1)
#             document.add_paragraph(f'Title: {contract.title}')
#             document.add_paragraph(f'First Name: {contract.first_name}')
#             document.add_paragraph(f'Last Name: {contract.last_name}')
#             # Сохранение документа во временном файле
#             temp_file_path = '/tmp/contract.docx'
#             document.save(temp_file_path)
#             # Отправка файла как HTTP-ответ для скачивания
#             with open(temp_file_path, 'rb') as file:
#                 response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = f'attachment; filename="{os.path.basename(temp_file_path)}"'
#                 return response
#         else:
#             return HttpResponse(_('Contract not found'), status=404)

#     def download_selected_word(self, request, queryset):
#         response = HttpResponse(content_type='application/zip')
#         response['Content-Disposition'] = 'attachment; filename="contracts.zip"'

#         with zipfile.ZipFile(response, 'w') as zip_file:
#             for contract in queryset:
#                 # Создание нового документа Word для каждого контракта
#                 document = Document()
#                 document.add_heading('Contract', level=1)
#                 document.add_paragraph(f'Title: {contract.title}')
#                 document.add_paragraph(f'First Name: {contract.first_name}')
#                 document.add_paragraph(f'Last Name: {contract.last_name}')
#                 # Сохранение документа во временном файле
#                 temp_file_path = f'/tmp/{contract.title}_{contract.first_name}_{contract.last_name}.docx'
#                 document.save(temp_file_path)
#                 # Добавление документа в ZIP-архив
#                 zip_file.write(temp_file_path, os.path.basename(temp_file_path))

#         return response
#     download_selected_word.short_description = _('Download Selected Word')

# admin.site.register(Contract, ContractAdmin)








# @admin.register(WorkSchedule)
# class WorkScheduleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user',)
#     search_fields = ('user__email',)
#     fields = (
#         'user', 'monday', 'tuesday', 
#         'wednesday', 'thursday', 'friday', 
#         'saturday', 'sunday', 
#         'custom', 
#         'custom_start_time', 'custom_end_time',
#         )