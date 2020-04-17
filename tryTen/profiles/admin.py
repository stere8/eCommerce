from django.contrib import admin
from .models import profile, userStripe,Role
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model = Role


class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile


class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe


admin.site.register(Role,RoleAdmin)
admin.site.register(profile,profileAdmin)
admin.site.register(userStripe,userStripeAdmin)