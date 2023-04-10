from django.contrib import admin

# Register your models here.

from .models import Topp
from .models import Joke

admin.site.register(Topp)
admin.site.register(Joke)