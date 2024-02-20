from applications.accounts.models import User
from rest_framework import serializers
from .models import *
from applications.accounts.serializers import ProfileAllSerializer
from django.contrib.auth import get_user_model
# from schedule.models import Event



User = get_user_model()



class EmployerProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EmployerCompany
        fields = [
            'id',
            'icon',
            'first_name',
            'last_name',
            'name',
            'description',
        ]

class EmployerCompanySerialzers(serializers.ModelSerializer):
    iin = serializers.CharField(required=False, allow_blank=True)
    icon = serializers.ImageField(required=False, use_url=True,allow_null=True)
  
    class Meta:
        model = EmployerCompany
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'name',
            'iin',
            'description',
            'icon',
        ]


    def get_url_icon(self, obj):  
        request = self.context.get('request')
        url_icon = obj.icon.url
        return request.build_absolute_uri(url_icon)
    
    
   

class EmployerUpdateSerialzers(serializers.ModelSerializer):
        first_name = serializers.CharField(required=False)
        last_name = serializers.CharField(required=False)
        name = serializers.CharField(required=False)
        iin = serializers.CharField(required=False, allow_blank=True)
        description = serializers.CharField(required=False, allow_blank=True)
        icon = serializers.ImageField(required=False, use_url=True,allow_null=True)


    
        class Meta:
            model = EmployerCompany
            fields = [
                'id',
                'first_name',
                'last_name',
                'name',
                'iin',
                'description',
                'icon',
            ]
        
        def update(self, instance, validated_data):
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.name = validated_data.get('name', instance.name)
            instance.iin = validated_data.get('iin', instance.iin)
            instance.description = validated_data.get('description', instance.description)
            instance.icon = validated_data.get('icon', instance.icon)
            instance.save()
            return instance


class LandNameSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = LandName
        fields = [
            'id',
            'land_name',
        ]

class BranchSerializers(serializers.ModelSerializer):


    class Meta:
        model = Branch
        fields = [
            'id',
            'branch_land_name',
            'city_name',
            'company',
            'name',
            'address',
            'link_address',
            'description',
        ]

    def update(self, instance, validated_data):
        branch_land_name = validated_data.pop('branch_land_name', None)
        city_name = validated_data.pop('city_name', None)

        if branch_land_name:
            instance.branch_land_name = branch_land_name
        elif city_name:
            # Assuming city_name is a free text input, not a foreign key
            instance.city_name = city_name

        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.link_address = validated_data.get('link_address', instance.link_address)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance
    


class BranchListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = [
            'id',
            'branch_land_name',
            'city_name',
            'name',
        ]

    



class PositionEmployeeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PositionEmployee
        fields = [
            'id',
            'name',
        ]


    


class VacancySerializers(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = [
            'branch',
            'position', 
            'duty', 
            'experience', 
            'clothingform', 
            'employee_count',
            'time_start', 
            'time_end', 
            'salary', 
            'increase_choices', 
            'description',
            'language_german',
            'language_english',

            ]
    

    def update(self, instance, validated_data):
        instance.branch = validated_data.get('branch', instance.branch)
        instance.position = validated_data.get('position', instance.position)
        instance.duty = validated_data.get('duty', instance.duty)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.clothingform = validated_data.get('clothingform', instance.clothingform)
        instance.employee_count = validated_data.get('employee_count', instance.employee_count)
        instance.time_start = validated_data.get('time_start', instance.time_start)
        instance.time_end = validated_data.get('time_end', instance.time_end)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.increase_choices = validated_data.get('increase_choices', instance.increase_choices)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class VacancyDetailSerializers(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='employer_company.user.id')
    employer_company_icon = serializers.ImageField(source='employer_company.icon')
    employer_company_name = serializers.CharField(source='employer_company.name')
    branch = serializers.CharField(source='branch.name')
    branch_city = serializers.CharField(source='branch.city.name')
    branch_address = serializers.CharField(source='branch.address')
    position = serializers.CharField(source='position.name')
    created_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vacancy
        fields = [
            'user_id', 
            'employer_company_name',
            'employer_company_icon',
            'branch',
            'branch_city',
            'branch_address',
            'position', 
            'duty', 
            'experience', 
            'clothingform', 
            'employee_count',
            'time_start', 
            'time_end', 
            'salary', 
            'increase_choices', 
            'description',
            'views_vacancy',
            'language_german',
            'language_english',
            'created_date',


            ]
    
    def get_created_date(self, obj):
        return obj.created_date.strftime("%d.%m.%Y")

    def get_employer_company_icon(self, obj):
        request = self.context.get('request')
        url_icon = obj.employer_company.icon.url
        return request.build_absolute_uri(url_icon)


class VacancyListSerializers(serializers.ModelSerializer):
    employer_company_icon = serializers.ImageField(source='employer_company.icon')
    employer_company_name = serializers.CharField(source='employer_company.name')
    branch = serializers.CharField(source='branch.name')
    branch_city = serializers.CharField(source='branch.city.name')
    branch_address = serializers.CharField(source='branch.address')
    position = serializers.CharField(source='position.name')
    created_date = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Vacancy
        fields = [
            'id',
            'employer_company_name',
            'employer_company_icon',
            'branch',
            'branch_city',
            'branch_address',
            'position', 
            'experience', 
            'employee_count',
            'time_start', 
            'time_end', 
            'salary', 
            'views_vacancy',
            'created_date',
            ]
    
    
    def get_created_date(self, obj):
        return obj.created_date.strftime("%d.%m.%Y")


class InvitationSerializers(serializers.ModelSerializer):
    user_profile = ProfileAllSerializer(source='user', read_only=True)
    created_date = serializers.SerializerMethodField(read_only=True)
    position = PositionEmployeeSerializers(source='vacancy.position', read_only=True)
    branch = BranchListSerializers(source='vacancy.branch', read_only=True)
    

    
    class Meta:
        model = Invitation
        fields = [
            'id',
            'vacancy',
            'user',
            'user_profile',
            'created_date',
            'position',
            'branch',
        ]

    def get_created_date(self, obj):
        return obj.created_date.strftime("%d.%m.%Y")

    def get_user_profile_icon(self, obj):
        request = self.context.get('request')
        url_icon = obj.user.icon.url
        return request.build_absolute_uri(url_icon)

