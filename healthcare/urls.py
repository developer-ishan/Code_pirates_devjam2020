from django.urls import path
from .views import doc_list_view

urlpatterns=[
    path('',doc_list_view.as_view(),name='new_doc')
]