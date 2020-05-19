from django.urls import path
from .views import *
app_name='community'

urlpatterns = [
    path('create',community_create_view.as_view(),name="create"),
    path('<slug:slug>/view',community_detail_view.as_view(),name="detail"),
    path('<slug:slug>/official',declare_official_community,name="official"),
    path('<slug:slug>/theme/<int:theme_num>/',community_theme,name="theme"),
    path('<slug:slug>/members',community_member_list.as_view(),name="members"),
    path('<slug:slug>/join',join_community,name="join"),
    path('<slug:slug>/leave',leave_community,name="leave"),
    path('<slug:slug>/update',community_update_view.as_view(),name="update"),
    path('<slug:slug>/delete',community_delete_view.as_view(),name="delete"),
    path('<slug:slug>/post/create',post_create_view.as_view(),name="create-post"),
    path('post/<int:pk>/update',post_update_view.as_view(),name="update-post"),
    path('post/<int:pk>/delete',post_delete_view.as_view(),name="delete-post"),
    #keep this "all" named url at the bottom
    path('<str:type>',community_list_view.as_view(),name="all"),
]