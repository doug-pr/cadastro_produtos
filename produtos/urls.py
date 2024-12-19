from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]