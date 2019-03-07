from django.contrib import admin

# Register your models here.
from .models import Ships
from .models import Positions

admin.site.register(Ships)
admin.site.register(Positions)
