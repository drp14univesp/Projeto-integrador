from django.shortcuts import render

def home(request):
    return render(request,'app_cad_usuarios/home.html')
