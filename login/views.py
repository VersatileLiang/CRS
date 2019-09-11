from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def user_login(request):
    return render(request, 'index.html')
