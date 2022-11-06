from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.create_message),
    re_path('delete/(?P<pk>(\d)+)/$', views.delete_message),
    re_path('edit/(?P<pk>(\d)+)/$', views.edit_message_content),
    re_path('get/(?P<pk>(\d)+)/$', views.get_message),
    path('get_list_for_user_chat/', views.get_messages_filter_user_chat),
    path('get_list_for_chat/', views.get_messages_filter_chat),
    re_path('mark_as_viewed/(?P<pk>(\d)+)/$', views.mark_message_as_viewed),
]
