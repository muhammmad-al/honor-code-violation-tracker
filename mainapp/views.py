from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index_view(request):
    is_site_admin = request.user.groups.filter(name='site_admin').exists()
    
    context = {'is_site_admin': is_site_admin}
    return render(request, 'index.html', context)

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')
