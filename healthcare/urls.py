from django.urls import path
from .views import doc_list_view
app_name = "healthcare"
urlpatterns=[
    path('',doc_list_view.as_view(),name='all')
]