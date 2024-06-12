from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def index(request):
    users = User.objects.all().order_by('-id')
    
    context = {
        'users': users
        }
    
    return render(request, 'users/index.html', context)

def create(request):
    
    form_action = reverse('users:create')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Usuário cadastrado')
            
            return redirect('users:index')
        
        context = {
        'form': form,
        'form_action': form_action
        }
        
        return render(request, 'users/create.html', context)
            
    
    form = UserForm()
    
    context = {
        'form': form,
        'form_action': form_action
    }
    
    return render(request, 'users/create.html', context)

def update(request):
    return render(request, 'users/create.html')

def delete(request):
    user = get_object_or_404(User, id=id)
    
    user.delete()
    
    return redirect('users:indec')

def login(request):
    return render(request, 'users/login.html')
