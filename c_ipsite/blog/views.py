# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Author, Entry

def index(request):
    ime_bloga = Blog.objects.get(pk=1)
    autor = Author.objects.get(pk=1)
    zadnji_naslov = Entry.objects.all().latest('id')
    lista_naslova = Entry.objects.all().order_by('datum_objave')[:5]

    return render_to_response('blog/index2.html', {'zadnji_naslov' : zadnji_naslov, 'ime_bloga' : ime_bloga, 'lista_naslova' : lista_naslova, 'autor' : autor })

# def detail(request, 
