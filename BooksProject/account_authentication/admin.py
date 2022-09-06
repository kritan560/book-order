from django.contrib import admin
from . models import AccountAuthentication
# Register your models here.
@admin.register(AccountAuthentication)
class AccountAuthenticationAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'logo', 'address']