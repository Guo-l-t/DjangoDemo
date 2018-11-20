from django.urls import path

from . import views

urlpatterns = [
    # ex: /birthday/
    path('', views.index, name='index'),
    # ex: /birthday/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /birthday/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /birthday/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]