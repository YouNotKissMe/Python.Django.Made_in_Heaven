from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'category', 'author')


admin.site.register(Publication, PublicationAdmin)
