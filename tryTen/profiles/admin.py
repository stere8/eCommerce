from django.contrib import admin
from .models import profile, userStripe
# Register your models here.


class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile


class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe


admin.site.register(profile,profileAdmin)
admin.site.register(userStripe,userStripeAdmin)