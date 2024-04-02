from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuario_view(request):
  if request.method == 'POST':
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.endereco = request.POST.get('endereco')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.condominio = request.POST.get('condominio')
    novo_usuario.save()

# exibir usuarios
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

# retornar os dados
    return render(request,'usuarios/usuarios.html', usuarios)

