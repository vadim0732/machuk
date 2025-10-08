from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(ListeningHistory)
admin.site.register(UserFavorite)

