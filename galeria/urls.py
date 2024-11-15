from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),  # Define a rota raiz para a função 'index'
    path('imagem/', imagem, name= 'imagem'),  # Define a rota '/imagem/' para a função 'imagem'
]
