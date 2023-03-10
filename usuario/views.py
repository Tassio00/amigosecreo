from django.shortcuts import redirect, render

from usuario.models import Usuario


def usuario(request):
    #mostra os usuarios
    
    return render (request, 'usuario_list.html')

def addUsuario(request):

    user = request.POST.get('user')
    email = request.POST.get('email')

    try:
        usuario = Usuario(nome = user, email = email)
        usuario.save()

        return redirect('/?status=1')
    except:
        return redirect('/?status=0')
    




