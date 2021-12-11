from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Anuncio

# Create your views here.
def home_view(request):
    anuncios = Anuncio.objects.all().order_by('-data_criacao')
    return render(request, "index.html", {'anuncios':anuncios})

def add_view(request):
    return render(request, "add.html")

def add_vaga(request):
    if request.method == 'POST':
        anuncio = Anuncio()
        anuncio.titulo = request.POST.get('title')
        anuncio.descricao = request.POST.get('description')
        anuncio.empresa = request.POST.get('company')
        anuncio.email = request.POST.get('email')
        anuncio.salario = request.POST.get('salary')
        anuncio.save()
        
        return redirect('home')
        
    else:
        return redirect('home')

def list_vaga(request, vaga_id):
    anuncio = Anuncio.objects.get(id=vaga_id)
    return render(request, 'detail.html', {'vaga':anuncio})

def search(request):
    anuncios = Anuncio.objects.filter(titulo__contains=request.POST.get('job'))
    return render(request, 'search.html', {'anuncios':anuncios})