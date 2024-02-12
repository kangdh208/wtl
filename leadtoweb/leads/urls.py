from django.urls import path, include
from leads.views import lead_create

urlpatterns = [
    path('create/', lead_create, name='lead_create'),
]