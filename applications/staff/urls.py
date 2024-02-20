from django.urls import path
from .views import GetAllvacanciesAPIView



urlpatterns = [
    path('vacancies/', GetAllvacanciesAPIView.as_view(), name='all-vacancies'),
]