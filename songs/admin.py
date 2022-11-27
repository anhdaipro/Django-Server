from django.contrib import admin
from .models import *
# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_filter = ('name', 'artist_name')
    search_fields = ['name','artist_name']
    list_display = ('id', 'name','artist_name','album','hasKaraoke','hasLyric')
admin.site.register(Song,SongAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Video)