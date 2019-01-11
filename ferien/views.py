from django.shortcuts import render
from django.utils import timezone
from ferien import models
import calendar
import holidays


def index(request):
    context = {
        'choices': models.SchoolHolidays.COUNTRY_CHOICES,
        'year': timezone.now().year
    }
    return render(request, 'ferien/index.html', context=context)


def country_calendar(request, year, location):
    country = location.split('-')[0]
    state = location.split('-')[1]
    bank_holidays = holidays.CountryHoliday(country, prov=state)
    context = {
        'year': year,
        'bank_holidays': bank_holidays,
    }
    return render(request, 'ferien/year_calendar.html', context=context)
