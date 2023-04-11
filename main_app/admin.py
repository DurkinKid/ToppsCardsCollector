from django.contrib import admin

# Register your models here.

from .models import Topp, Joke, Offer


admin.site.register(Topp)
admin.site.register(Joke)
admin.site.register(Offer)