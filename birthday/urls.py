from django.urls import path

from . import views

urlpatterns = [
    # ex: /birthday/
    path('', views.index, name='index'),
    # ex: /birthday/5/
    path('add/', views.add, name='add'),
    # ex: /birthday/5/results/

]