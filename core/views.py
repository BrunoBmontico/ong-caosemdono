from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def donation(request):
    return render(request, 'core/donation.html')

def contact(request):
    return render(request, 'core/contact.html')

def clinic(request):
    return render(request, 'core/clinic.html')

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
    
def adopt(request):

    if request.method == 'GET':
        return render(request, 'core/adopt.html')
    else:
        profissao = request.POST.get('profissao')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nasc = request.POST.get('nasc')
        cep = request.POST.get('cep')
        bairro = request.POST.get('bairro')
        endereco = request.POST.get('endereco')
        dog_name = request.POST.get('dog_name')

        adopt = Adopt(
            profissao = profissao,
            nome = nome,
            email = email,
            nasc = nasc,
            cep = cep,
            bairro = bairro,
            endereco = endereco,
            dog_name = dog_name
        )

        adopt.save()
        return redirect('/success/')
    
def sponsor(request):

    if request.method == 'GET':
        return render(request, 'core/sponsor.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nasc = request.POST.get('nasc')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        bairro = request.POST.get('bairro')
        endereco = request.POST.get('endereco')
        dog_name = request.POST.get('dog_name')
        valor_mensal = request.POST.get('valor_mensal')
        recebimento = request.POST.get('recebimento')

        sponsor = Sponsor(
            nome = nome,
            email = email,
            cpf = cpf,
            cep = cep,
            bairro = bairro,
            endereco = endereco,
            dog_name = dog_name,
            valor_mensal = valor_mensal,
            recebimento = recebimento,
        )

        sponsor.save()
        return redirect('/success/')