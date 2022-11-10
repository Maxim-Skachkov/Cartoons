from django.contrib import admin
from . import models
# Register your models here.


class PrepopulatedURL(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


admin.site.register(models.Cartoon, PrepopulatedURL)
admin.site.register(models.CartoonCategory, PrepopulatedURL)
admin.site.register(models.Episode, PrepopulatedURL)
admin.site.register(models.Screenshot, PrepopulatedURL)
admin.site.register(models.Actor, PrepopulatedURL)


