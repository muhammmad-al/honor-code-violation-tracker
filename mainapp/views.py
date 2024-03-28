from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from allauth.socialaccount.models import SocialAccount

from django.shortcuts import render, redirect
from .forms import HonorCodeViolationForm
from .models import HonorCodeViolation

from django.core.mail import send_mail


# Imported + printed on view!
from django.contrib.sites.shortcuts import get_current_site


def violation_detail(request, id):
    violation = get_object_or_404(HonorCodeViolation, id=id)
    if violation.status == 'new':
        violation.status = 'in_progress'
        violation.save()
    return render(request, 'violation_detail.html', {'violation': violation})


def mark_resolved(request, id):
    violation = get_object_or_404(HonorCodeViolation, id=id)
    if request.method == 'POST':
        resolution_notes = request.POST.get('resolution_notes')
        violation.resolution_notes = resolution_notes
        violation.status = 'resolved'
        violation.save()
    return HttpResponseRedirect(reverse('admin_dashboard_url'))


@login_required
def account_details(request):
    return render(request, 'account_details.html', {'user': request.user})


class IndexView(View):
    def get(self, request):
        is_site_admin = request.user.groups.filter(name='site_admin').exists()
        current_site = get_current_site(request)
        context = {
            'is_site_admin': is_site_admin,
            'current_site': current_site
        }
        return render(request, 'index.html', context)


class UserLoginView(View):
    def get(self, request):
        form = HonorCodeViolationForm()
        return render(request, 'user_dashboard.html', {'form': form})

    def post(self, request):
        form = HonorCodeViolationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'Subject here',
                'Here is the message.',
                'anhtule7913@gmail.com',  # From email
                [request.user.email],  # To email list
                fail_silently=False,
            )
            
    
            return redirect('index')  # Redirect to a confirmation page or back to form
        return render(request, 'user_dashboard.html', {'form': form})


class AdminLoginView(View):
    def get(self, request):
        violations = HonorCodeViolation.objects.all()
        return render(request, 'admin_dashboard.html', {'violations': violations})
