from django.contrib import admin

from app.models import AviatorBet, AviatorDeposit, AviatorProfile

# Register your models here.
admin.site.register(AviatorProfile)
admin.site.register(AviatorDeposit)
admin.site.register(AviatorBet)