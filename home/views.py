from django.shortcuts import render

# Create your views here.

def login_page(request):
    
    if request.method == 'POST':
        pass

    return render(request, 'login.html')

def register_page(request):
    
    if request.method == 'POST':
        data = request.POST
         

    return render(request, 'register.html')

def home_page(request):
    return render(request,template_name='home.html')