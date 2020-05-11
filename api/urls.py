from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import list_gate_entry_api,create_gate_entry_api

app_name='api'
router = DefaultRouter()

urlpatterns=[
    path('',include(router.urls)),
    path('list',list_gate_entry_api.as_view(),name='list_entry_api'),
    path('entry/<str:regno>/',create_gate_entry_api,name='create_entry_api'),
]