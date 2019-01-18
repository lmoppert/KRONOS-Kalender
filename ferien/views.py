from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from ferien import models
import calendar


def index(request):
    context = {
        'choices': models.Country.objects.all(),
        'year': timezone.now().year,
    }
    return render(request, 'ferien/index.html', context=context)


def country_calendar(request, year, location):
    yearcal = calendar.Calendar()
    year_calendar = []
    today = timezone.now()
    for month in range(1, 13):
        year_calendar.append((yearcal.monthdatescalendar(year, month),
                              calendar.month_name[month], month))
    country = get_object_or_404(models.Country, iso=location)
    bank_holidays = country.holidays
    timezone.datetime(year, 1, 1).date() in bank_holidays
    holiday_list = (
        list(bank_holidays.items())[:len(bank_holidays)//2],
        list(bank_holidays.items())[len(bank_holidays)//2:])
    school_holidays = []
    for holiday in models.SchoolHolidays.objects.filter(country__iso=location):
        school_holidays.extend(holiday.get_holidays())
    context = {
        'today': today.date(),
        'kw': str(today.isocalendar()[1]),
        'year': year,
        'state': country.region,
        'bank_holidays': bank_holidays,
        'school_holidays': school_holidays,
        'year_calendar': year_calendar,
    }
    return render(request, 'ferien/year_calendar.html', context=context)
