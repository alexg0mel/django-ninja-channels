from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import SettingsOne, SettingsTwo, SettingsHolder


@admin.register(SettingsOne)
class SettingsOneAdmin(ModelAdmin):
    pass


@admin.register(SettingsTwo)
class SettingsTwoAdmin(ModelAdmin):
    pass


@admin.register(SettingsHolder)
class SettingsHolderAdmin(ModelAdmin):
    pass
