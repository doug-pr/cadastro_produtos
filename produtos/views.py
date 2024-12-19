from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def cadastrar(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastrar.html', {'status': status})
    elif request.method == 'POST':
        nome_produto = request.POST.get('produto')
        preco = request.POST.get('preco')

        prod = Produto(
            produto = nome_produto,
            preco = preco
        )
        prod.save()
        return redirect('/produtos/cadastrar?status=1')
    
def listar(request):
    nome_produto = request.GET.get('nome_produto')
    preco_produto = request.GET.get('preco_produto')

    produtos = Produto.objects.all()

    if nome_produto:
        produtos = produtos.filter(produto__contains=nome_produto)

    if preco_produto:
        produtos = produtos.filter(preco_gte=preco_produto)
    
    return render(request, 'listar.html', {'produtos': produtos})

def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produtos/listar')

def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'detalhes.html', {'produto': produto})

def editar(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'editar.html', { 'produto': produto })

def atualizar(request, id):
    nome_produto = request.POST.get('produto')
    preco = request.POST.get('preco')
    produto = Produto.objects.get(id=id)
    produto.nome = nome_produto
    produto.preco = preco
    produto.save()
    return redirect('../../produtos/listar')

