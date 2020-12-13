from django.contrib import admin

from hostelservices.models import HostelService, SellingPrice, PurchasePrice

admin.site.register(HostelService)
admin.site.register(SellingPrice)
admin.site.register(PurchasePrice)