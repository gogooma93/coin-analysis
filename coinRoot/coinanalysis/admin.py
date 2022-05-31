from django.contrib import admin

from coinanalysis.models import BitcoinER
admin.site.register(BitcoinER)

from coinanalysis.models import QnA
admin.site.register(QnA)
# Register your models here.
