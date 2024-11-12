from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('team/', views.team, name='team'),
    path('volunteers/', views.volunteers, name='volunteers'),
]