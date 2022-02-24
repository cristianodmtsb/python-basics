from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato


def index(request):
    contatos_lista = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos_lista, 10)  # Show 10 contacts per page

    page = request.GET.get('p')
    contatos_lista = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos' : contatos_lista
    })

def single_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) # buscando dados ou retorna 404

    if not contato.mostrar:
        Http404()
    else:
        return render(request, 'contatos/single.html', {
            'contato' : contato
        })

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos_lista = Contato.objects.annotate(

    )
    paginator = Paginator(contatos_lista, 10)  # Show 10 contacts per page

    page = request.GET.get('p')
    contatos_lista = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos_lista
    })