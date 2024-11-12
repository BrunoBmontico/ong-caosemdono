from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def success(request):
    return render(request, 'core/success.html')

def home_page(request):
    return render(request, 'core/home_page.html')

def team(request):
    return render(request, 'core/team.html')

def volunteers(request):

    if request.method == 'GET':
        return render(request, 'core/volunteers.html')
    else:
        profissao = request.POST.get('profissao')
        empresa = request.POST.get('empresa')
        cargo = request.POST.get('cargo')
        habilitação = request.POST.get('habilitação')
        dirige = request.POST.get('dirige')
        possui_carro = request.POST.get('possui_carro')
        cargo_voluntario = request.POST.get('cargo_voluntario')

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nasc = request.POST.get('nasc')
        whats = request.POST.get('whats')
        cep = request.POST.get('cep')
        bairro = request.POST.get('bairro')
        endereco = request.POST.get('endereco')

        volunteer = Volunteers(
            profissao = profissao,
            empresa = empresa,
            cargo = cargo,
            habilitação = habilitação,
            dirige = dirige,
            possui_carro = possui_carro,
            cargo_voluntario = cargo_voluntario,
            nome = nome,
            email = email,
            nasc = nasc,
            whats = whats,
            cep = cep,
            bairro = bairro,
            endereco = endereco,
        )

        volunteer.save()
        return redirect('/success/')