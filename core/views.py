from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'core/home_page.html')

def team(request):
    return render(request, 'core/team.html')
