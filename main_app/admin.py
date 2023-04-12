from django.contrib import admin

# Register your models here.

from .models import Topp, Joke, Offer, Company


admin.site.register(Topp)
admin.site.register(Joke)
admin.site.register(Offer)
admin.site.register(Company)