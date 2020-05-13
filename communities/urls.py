from django.urls import path
from .views import *
app_name='community'

urlpatterns = [
    path('',community_list_view.as_view(),name="all"),
    path('create',community_create_view.as_view(),name="create"),
    path('<slug:slug>/',community_detail_view.as_view(),name="detail"),
    path('<slug:slug>/update',community_update_view.as_view(),name="update"),
    path('<slug:slug>/delete',community_delete_view.as_view(),name="delete"),
    path('<slug:slug>/post/create',post_create_view.as_view(),name="create-post"),
    path('post/<int:pk>/update',post_update_view.as_view(),name="update-post"),
    path('post/<int:pk>/delete',post_delete_view.as_view(),name="delete-post"),
    
]