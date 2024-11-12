from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('success/', views.success, name='success'),
    path('team/', views.team, name='team'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('adopt/', views.adopt, name='adopt'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('clinic/', views.clinic, name='clinic'),
]