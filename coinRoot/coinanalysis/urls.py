from django.urls import path
from . import views

app_name = 'coinanalysis'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('coin/', views.coins, name='coins'),
    path('chart/', views.bitcoiner_graph, name='chart'),
    path('qna/', views.qna, name='qna'),
]