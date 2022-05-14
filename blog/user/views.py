from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import User
from rest_framework.response import Response


# Create your views here.
class GetUserInfo(ListView):
    queryset = User.objects.all()

    def get(self, request):
        return HttpResponse(User.objects.all())