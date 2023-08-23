from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
]
    

