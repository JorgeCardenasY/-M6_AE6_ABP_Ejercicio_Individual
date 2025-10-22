from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def admin_panel(request):
    return render(request, 'admin.html')