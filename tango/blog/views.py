# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Author, Entry

def index(request):
    ime_bloga = Blog.objects.get(pk=1)
    autor = Author.objects.get(pk=1)
    zadnji_naslov = Entry.objects.all().latest('id')
    lista_naslova = Entry.objects.all().order_by('-datum_objave')[:5]

    return render_to_response('blog/index2.html', {'zadnji_naslov' : zadnji_naslov, 'ime_bloga' : ime_bloga, 'lista_naslova' : lista_naslova, 'autor' : autor })

def year_archive(request, year):
    ime_bloga = Blog.objects.get(pk=1)
    ent = Entry.objects.all().filter(datum_objave__year=year)
    return render_to_response('blog/detail.html', {'ent' : ent, 'ime_bloga': ime_bloga })

def year_month_archive(request, year, month):
    ime_bloga = get_object_or_404(Blog, pk=1)
    ent = Entry.objects.all().filter(datum_objave__year=year, datum_objave__month=month)
    return render_to_response('blog/year_month.html', {'ent': ent, 'ime_bloga': ime_bloga })

def day_archive(request, year, month, day):
    ime_bloga = get_object_or_404(Blog, pk=1)
    ent = Entry.objects.all().filter(datum_objave__year=year, datum_objave__month=month, datum_objave__day=day)
    return render_to_response('blog/day_archive.html', {'ent': ent, 'ime_bloga': ime_bloga })

def post_detail(request, year, month, day, slug):
    ime_bloga = get_object_or_404(Blog, pk=1)
    ent = Entry.objects.all().filter(datum_objave__year=year, datum_objave__month=month, datum_objave__day=day, slug=slug)
    return render_to_response('blog/post_detail.html', {'ent': ent, 'ime_bloga': ime_bloga })

