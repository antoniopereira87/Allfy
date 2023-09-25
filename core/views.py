from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')