from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Income, Expense
from .choices import CATEGORIA



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
            return redirect('user_area', id=user.profile.id)
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def user_area(request, id):
    profile = Profile.objects.filter(id=id).first()
    incomes = profile.income.all()
    expenses = profile.expense.all()
    result_income = 0
    result_expense = 0
    categories_result = {
        'Alimentação':0.0,
        'Transporte':0.0,
        'Moradia':0.0,
        'Vestuário':0.0,
        'Assinaturas':0.0,
        'Saúde':0.0,
        'Lazer':0.0,
    }
    for income in incomes:
        result_income += income.valor

    for expense in expenses:
        result_expense += expense.valor
        categoria = expense.categoria
        if categoria == 'alimentacao':
            categories_result ['Alimentação'] += expense.valor
        elif categoria == 'transporte':
            categories_result ['Transporte'] += expense.valor
        elif categoria == 'moradia':
            categories_result ['Moradia'] += expense.valor
        elif categoria == 'vestuario':
            categories_result ['Vestuário'] += expense.valor
        elif categoria == 'assinaturas':
            categories_result ['Assinaturas'] += expense.valor
        elif categoria == 'saude':
            categories_result ['Saúde'] += expense.valor
        elif categoria == 'lazer':
            categories_result ['Lazer'] += expense.valor

    balance = result_income - result_expense

    context = {
        'profile':profile,
        'incomes':incomes,
        'expenses':expenses,
        'balance':balance,
        'categories_result':categories_result
    }
    return render(request, 'user_area.html', context)

@login_required
def cadastrar_receita(request, id):
    if request.method == "POST":
        valor = request.POST["valor"]
        valor = valor.replace(',','.')
        valor = float(valor)
        profile = Profile.objects.filter(id=id).first()
        descricao = request.POST["descricao"]
        income = Income.objects.create(valor=valor, descricao=descricao, profile=profile)
        income.valor = valor
        income.descricao = descricao
        income.save()
        return redirect('user_area', id=id)
    context = {
        'id':id
    }
    return render(request, 'cadastrar_receita.html', context)

@login_required
def alterar_receita(request, id):
    income = Income.objects.filter(id=id).first()
    if request.method == "POST":
        valor = request.POST["valor"]
        valor = valor.replace(',','.')
        valor = float(valor)
        descricao = request.POST["descricao"]
        income.valor = valor
        income.descricao = descricao
        income.save()
        return redirect('user_area', id=income.profile.id)
    context ={
        'income':income,
        'id':income.profile.id
    }
    return render(request, 'cadastrar_receita.html', context)



@login_required
def apagar_receita(request, id):
    income = Income.objects.get(id=id)
    income.delete()
    return redirect('buscar')


@login_required
def cadastrar_despesa(request, id):
    if request.method == "POST":
        valor = request.POST["valor"]
        valor = valor.replace(',', '.')
        valor = float(valor)
        profile = Profile.objects.filter(id=id).first()
        categoria = request.POST["categoria"]
        descricao = request.POST["descricao"]
        expense = Expense.objects.create(valor=valor, categoria=categoria, descricao=descricao, profile=profile)
        expense.save()
        return redirect('user_area', id=id)
    context = {
        'id':id,    
        'categoria':CATEGORIA
    }
    return render(request, 'cadastrar_despesa.html', context)

@login_required
def alterar_despesa(request, id):
    expense = Expense.objects.filter(id=id).first()
    if request.method == "POST":
        valor = request.POST["valor"]
        valor = valor.replace(',', '.')
        valor = float(valor)
        categoria = request.POST["categoria"]
        descricao = request.POST["descricao"]
        expense.valor = valor
        expense.descricao = descricao
        expense.categoria = categoria
        expense.save()
        return redirect('user_area', id=expense.profile.id)
    context ={
        'categoria':CATEGORIA,
        'expense':expense,
        'id':expense.profile.id
    }
    return render(request, 'cadastrar_despesa.html', context)

@login_required
def apagar_despesa(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('buscar')


@login_required
def buscar(request):
    profile = request.user.profile
    id = profile.id
    
    tipo = request.GET.get('tipo', None)
    categoria = request.GET.get('categoria', None)
    valor = request.GET.get('valor', None)
    data_query = {'profile__id':id,}
    if categoria:
        data_query['categoria'] = categoria
    
    if valor:
        data_query['valor'] = valor

    receitas = None
    despesas = None

    if tipo == 'receitas':
        receitas = Income.objects.filter(**data_query)

    elif tipo == 'despesas':
        despesas = Expense.objects.filter(**data_query)

    else:
        receitas = Income.objects.filter(**data_query)
        despesas = Expense.objects.filter(**data_query)
    
    context = {
        'id':id,
        'receitas':receitas,
        'despesas':despesas,
        'categoria':CATEGORIA
    }
    return render(request, 'buscar.html', context)
