from rest_framework import serializers
from applications.core.models import *


class PositionEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionEmployee
        fields = ['id', 'name']

class EmployerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerCompany
        fields = ['id', 'name']

class LandNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandName
        fields = ['land_name']

class BranchSerializer(serializers.ModelSerializer):
    branch_land_name = LandNameSerializer()
    
    class Meta:
        model = Branch
        fields = ['branch_land_name', 'name', 'city_name']


class GetAllVacanciesSerializers(serializers.ModelSerializer):
    employer_company = EmployerCompanySerializer()
    position = PositionEmployeeSerializer()
    branch = BranchSerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'
 