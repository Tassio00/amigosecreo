from django.shortcuts import redirect, render

from usuario.models import Usuario

def home(request):
    userList = Usuario.objects.all()
    context = {
        'userList': userList,
    }
    
    return render (request, 'home.html', context )

def dellUsuario(request, id):
    
    
    try:
        usuarioDeletado = Usuario.objects.get(pk=id)
        usuarioDeletado.delete()

        return redirect('/?status=del')
    except:
        return redirect('/?status=0')


def editUsuario(request, id):
    try:
        usuarioEdit = Usuario.objects.get(pk=id)

        return redirect('/?status=edit')
    except:
        return redirect('/?status=0')
        

