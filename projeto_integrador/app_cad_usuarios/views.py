from django.shortcuts import render, get_object_or_404, redirect 
from .models import Usuario
from django.urls import reverse

def home(request):
    return render(request,'usuarios/home.html')

def usuario_view(request):
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.endereco = request.POST.get('endereco')
        novo_usuario.cep = request.POST.get('cep')
        novo_usuario.condominio = request.POST.get('condominio')
        novo_usuario.save()
        return redirect('exibir_usuarios')

    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def exibir_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/exibir_usuarios.html', {'usuarios': usuarios})

def delete_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario = id_usuario)
    if request.method == 'POST':
        usuario.delete()
        
        return redirect(reverse('listagem_usuarios'))
    
    return render(request, 'usuarios/confirmar_delete.html', {'usuario': usuario})

def atualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome', usuario.nome)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.endereco = request.POST.get('endereco', usuario.endereco)
        usuario.cep = request.POST.get('cep', usuario.cep)
        usuario.condominio = request.POST.get('condominio', usuario.condominio)
        usuario.save()
        
        return redirect('listagem_usuarios')
    
    return render(request, 'usuarios/atualizar_usuario.html', {'usuario': usuario})