from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    return render(request, 'index.html')

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'cadastrar.html'

def cadastrar(request):
    return render(request, 'cadastrar.html')