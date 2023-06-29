from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.
def home (request):
    return render( request, 'home.html')

@login_required
def products (request):
    return render( request, 'products.html')

def exit (request):
    logout(request)
    return redirect ('home')

def register(request):
    data = {
        'form': CustumUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustumUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html',data)

def datosus (request):
    user = User.objects.all()
    data = {
        'user': user,
    }
    return render(request,'ver_user.html',data)

def editaruser (request, pk):

    data = {
        'form': editarUser(),
        'title' : 'Editar Rol Usuarios'
    }
    editarrol = User.objects.get(id=pk)
    if request.method == 'POST':
        formeditus = editarUser(data=request.POST, instance=editarrol)
        if formeditus.is_valid():
            formeditus.save()
            

            return redirect('verus')

            

    return render(request, 'editaruser.html', data)