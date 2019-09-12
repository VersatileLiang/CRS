from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sign/signPage.html')

def index1(request):
    return None