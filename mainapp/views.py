from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from allauth.socialaccount.models import SocialAccount


def index(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from .forms import HonorCodeViolationForm
from .models import HonorCodeViolation

class UserLoginView(View):
    def get(self, request):
        form = HonorCodeViolationForm()
        return render(request, 'user_login.html', {'form': form})

    def post(self, request):
        form = HonorCodeViolationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a confirmation page or back to form
        return render(request, 'user_login.html', {'form': form})

class AdminLoginView(View):
    def get(self, request):
        violations = HonorCodeViolation.objects.all()
        return render(request, 'admin_login.html', {'violations': violations})
