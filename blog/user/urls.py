from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('get_user_info/', views.GetUserInfo.as_view())
]