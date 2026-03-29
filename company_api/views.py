from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_page(request):
    return render(request, 'dashboard.html')

def login_page(request):
    return render(request, 'login.html')