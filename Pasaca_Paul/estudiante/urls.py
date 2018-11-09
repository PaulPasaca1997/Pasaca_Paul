
from django.urls import path

from . import views
#importa todo lo del views


urlpatterns = [
    path('', views.principal,name='usuarios'),
    path('crear/', views.crear, name='crear'),

]
