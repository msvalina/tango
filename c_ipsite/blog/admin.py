from blog.models import Blog, Author, Entry
from django.contrib import admin


class EntryInline(admin.StackedInline):
    model = Entry
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
    prepopulated_fields = {'slug': ('naslov',)}

admin.site.register(Blog, BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'email']

admin.site.register(Author, AuthorAdmin)

admin.site.register(Entry)
    

