from django.db import models
from django.template.defaultfilters import slugify
import datetime


# Create your models here.

class Blog(models.Model):
    ime_bloga = models.CharField(max_length=100)
    opis_bloga = models.TextField()

    def __unicode__(self):
        return self.ime_bloga

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    naslov = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, help_text='Jedinstvena vrijednost kreirana iz naslova za potrebe URLa') 
    body_tekst = models.TextField()
    datum_objave = models.DateTimeField(default=datetime.datetime.now)
    datum_izmjene = models.DateTimeField()
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.naslov

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), { 
            'year' : self.datum_objave.year, 
            'month': self.datum_objave.strftime('%m'), 
            'day' : self.datum_objave.strftime('%d'),
            'slug' : self.slug
            })
