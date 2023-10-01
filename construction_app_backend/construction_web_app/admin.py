from django.contrib import admin
from .models import Region, Material, Favorite, Trade, Subtrade

# Register your models here.
admin.site.register(Region)
admin.site.register(Material)
admin.site.register(Favorite)
admin.site.register(Trade)
admin.site.register(Subtrade)
