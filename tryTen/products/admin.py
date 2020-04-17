from django.contrib import admin
from .models import product, category,image
# Register your models here.


class productAdmin(admin.ModelAdmin):
    class Meta:
        model = product


class categoryAdmin(admin.ModelAdmin):
    class Meta:
        model = category


admin.site.register(image)
admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)