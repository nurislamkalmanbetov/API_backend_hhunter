from rest_framework import generics
from applications.core.models import Vacancy
from .serializers import GetAllVacanciesSerializers



class GetAllvacanciesAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = GetAllVacanciesSerializers
    