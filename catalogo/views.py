from django.shortcuts import render, get_object_or_404
from .models import ItemCarrinho, Produto, Carrinho
from django.shortcuts import redirect, get_object_or_404
from .forms import ItemCarrinhoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'catalogo/lista_produtos.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    form = ItemCarrinhoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            carrinho, criado = Carrinho.objects.get_or_create(user=request.user)
            item_carrinho, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
            item_carrinho.quantidade += form.cleaned_data['quantidade']
            item_carrinho.save()
            return redirect('ver_carrinho')
    
    context = {
        'produto': produto,
        'form': form,
    }
    return render(request, 'catalogo/detalhes_produto.html', context)

def ver_carrinho(request):
    carrinho, criado = Carrinho.objects.get_or_create(user=request.user)
    itens_carrinho = carrinho.itemcarrinho_set.all()
    context = {
        'carrinho': carrinho,
        'itens_carrinho': itens_carrinho,
    }
    return render(request, 'catalogo/ver_carrinho.html', context)


def adicionar_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    carrinho, criado = Carrinho.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ItemCarrinhoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']

            # Verifique se o produto já está no carrinho
            item_carrinho, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
            
            # Atualize a quantidade do item no carrinho
            item_carrinho.quantidade += quantidade
            item_carrinho.save()

            # Depois de adicionar o item ao carrinho, redirecione o usuário para a página desejada
            return redirect('detalhes_produto', produto_id=produto_id)
    else:
        form = ItemCarrinhoForm()

    context = {
        'produto': produto,
        'form': form,
    }

    return render(request, 'catalogo/detalhes_produto.html', context)
