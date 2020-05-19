from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import list_gate_entry_api,create_gate_entry_api,show_tick_api,set_tick_to_true

app_name='api'
router = DefaultRouter() 

urlpatterns=[
    path('',include(router.urls)),
    path('tick-status/<str:regno>/',show_tick_api,name='tick-status'),
    path('tick-status/<str:regno>/true',set_tick_to_true,name='tick-toggle'),
    # path('tick-status/<str:regno>/false',set_tick_to_false,name='tick-false'),
    path('list',list_gate_entry_api,name='list_entry_api'),
    # path('list',list_gate_entry_api.as_view(),name='list_entry_api'),
    path('entry/<str:regno>/',create_gate_entry_api,name='create_entry_api'),
]