from django.urls import path
from .views import IncidentList, IncidentDetail

urlpatterns = [
    path('incidents', IncidentList.as_view()),
    path('incidents/<int:id>', IncidentDetail.as_view()),
]
