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
    yearcal = calendar.Calendar()
    year_calendar = []
    for month in range(1, 13):
        year_calendar.append((yearcal.monthdatescalendar(year, month),
                              calendar.month_name[month], month))
    country = location.split('-')[0]
    state = location.split('-')[1]
    bank_holidays = holidays.CountryHoliday(country, prov=state)
    school_holidays = []
    for holiday in models.SchoolHolidays.objects.filter(country=location):
        school_holidays.extend(holiday.get_holidays())
    context = {
        'year': year,
        'bank_holidays': bank_holidays,
        'school_holidays': school_holidays,
        'year_calendar': year_calendar,
    }
    return render(request, 'ferien/year_calendar.html', context=context)
