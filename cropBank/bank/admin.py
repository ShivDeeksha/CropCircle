# admin.py

from django.contrib import admin
from . import models

class BankImageInline(admin.TabularInline):
    model = models.BankImage

class BankCommodityInline(admin.TabularInline):
    model = models.BankCommodity

@admin.register(models.CropBank)
class CropBankAdmin(admin.ModelAdmin):
    inlines = [BankImageInline, BankCommodityInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type', 'is_verified')
    list_filter = ('is_verified',)
    actions = ['mark_verified']

    def mark_verified(modeladmin, request, queryset):
        # Mark selected users as verified
        queryset.update(is_verified=True)

    mark_verified.short_description = "Mark selected users as verified"

admin.site.register(models.User, UserAdmin)

# Register your models here if you haven't already
admin.site.register(models.BankImage)
admin.site.register(models.BankCommodity)

