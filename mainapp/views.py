from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from allauth.socialaccount.models import SocialAccount


def index(request):
    return render(request, 'index.html')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'user_login.html')


class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')
