from django.contrib import admin
from .models import PublicationAd


@admin.register(PublicationAd)
class PublicationAdAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']
