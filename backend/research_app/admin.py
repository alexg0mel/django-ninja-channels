from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import Country, Region, City


class CityInline(TabularInline):
    model = City
    extra = 0
    ordering = ['name']


class RegionInline(TabularInline):
    model = Region
    extra = 0
    ordering = ['name']


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]
    search_fields = ['name', 'regions__name', 'regions__cities__name']
    inlines = [RegionInline]


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = [field.name for field in Region._meta.fields]
    search_fields = ['name', 'country__name', 'cities__name']
    inlines = [CityInline, ]


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = [field.name for field in City._meta.fields]
    search_fields = ['name', 'region__name', 'region__country__name']

