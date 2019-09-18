from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def login_success(request):
    name=request.POST.get("name")
    password=request.POST.get("password")
    if(name=="admin"):
        if(password=="admin"):
            return render(request, 'reptile/reptilePage.html')
        else:
            return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')

