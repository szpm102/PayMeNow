from django.contrib import admin
from .models import SzpmApiOutstandingTransaction,SzpmApiMobileUser
# Register your models here.

admin.site.register(SzpmApiOutstandingTransaction)
admin.site.register(SzpmApiMobileUser)