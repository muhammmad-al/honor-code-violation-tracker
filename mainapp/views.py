from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from allauth.socialaccount.models import SocialAccount


def index(request):
    return render(request, 'index.html')


class UserLoginView(View):
    template_name = 'user_login.html'

    def get(self, request, *args, **kwargs):
        context = {'provider_login_url': SocialAccount.get_provider('google').get_login_url(request, next=None, **{})}
        return render(request, self.template_name, context)


class AdminLoginView(View):
    template_name = 'admin_login.html'

    @login_required
    def get(self, request, *args, **kwargs):
        context = {'username': request.user.username}
        return render(request, self.template_name, context)
