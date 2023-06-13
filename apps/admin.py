from django.contrib import admin

from apps.models import AModel


# Register your models here.
@admin.register(AModel)
class AADmin(admin.ModelAdmin):
    pass
