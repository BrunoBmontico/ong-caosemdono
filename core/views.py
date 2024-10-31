from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'core/home_page.html')
