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

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class BranchSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    
    class Meta:
        model = Branch
        fields = ['name', 'city']


class GetAllVacanciesSerializers(serializers.ModelSerializer):
    employer_company = EmployerCompanySerializer()
    position = PositionEmployeeSerializer()
    branch = BranchSerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'
 