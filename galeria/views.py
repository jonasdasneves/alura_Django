from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    dados = {
    1 : {"nome":"Nebulosa de Karina",
         "legenda":"webtelescope.org / NASA / james Webb"},
    2 : {"nome":"Galáxia ngc 1079",
         "legenda":"nasa.org / NASA / Hubble"}
}
    return render(request, 'galeria/index.html',{"cards":dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')

