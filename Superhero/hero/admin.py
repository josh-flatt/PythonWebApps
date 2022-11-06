from django.contrib import admin

from .models import Superhero, Article, Author

admin.site.register(Superhero)
admin.site.register(Article)
admin.site.register(Author)
