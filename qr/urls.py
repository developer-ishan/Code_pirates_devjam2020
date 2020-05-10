from django.urls import path
from .views import generate_qr_view
app_name = 'qr'
urlpatterns=[
    path('',generate_qr_view,name="generateqr")
]