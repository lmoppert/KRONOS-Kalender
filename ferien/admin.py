from django.contrib import admin
from ferien import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    model = models.Country
    extra = 0


@admin.register(models.SchoolHolidays)
class SchoolHolidaysAdmin(admin.ModelAdmin):
    model = models.SchoolHolidays
    extra = 0
    list_display = ('__str__', 'first_holiday', 'last_holiday')
    list_filter = ('name', 'country')
