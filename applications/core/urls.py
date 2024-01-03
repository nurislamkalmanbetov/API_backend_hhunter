from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'events', EventViewSet)

urlpatterns = [ 
    path('employercompany/', EmployerCompanyAPIView.as_view(), name='employercompany'),
]
