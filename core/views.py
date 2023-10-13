from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'index.html')

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'cadastrar.html'

def cadastrar(request):
    if request.method == "POST":
        POST = request.POST
        email = POST.get("email")
        first_name = POST.get("first_name")
        last_name = POST.get("last_name")
        password = POST.get("password1")
        confirm_password = POST.get("password2")
        if password == confirm_password:
            user = User.objects.create_user(email=email, username=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')
    return render(request, 'cadastrar.html')

def access_login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_area')
    return render(request, 'login.html')

def user_area(request):
    return render(request, 'user_area.html')