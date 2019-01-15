from django.utils.translation import ugettext_lazy as _
from django.db import models
import datetime


class Country(models.Model):
    """List of countries supported by the holiday class and the school holiday
       table
    """
    STATE = 's'
    PROVINCE = 'p'
    REGION_TYPES = (
        (STATE, 'State'),
        (PROVINCE, 'Province'),
        ('', 'No Regions defined'),
    )
    country = models.CharField(max_length=100, verbose_name=_("Country"))
    country_code = models.CharField(max_length=3, blank=True,
                                    verbose_name=_("Country Code"))
    region = models.CharField(max_length=100, blank=True,
                              verbose_name=_("Region"))
    region_code = models.CharField(max_length=3, blank=True,
                                   verbose_name=_("Region Code"))
    region_type = models.CharField(max_length=1, choices=REGION_TYPES,
                                   blank=True, verbose_name=_("Region Type"))

    class Meta:
        ordering = ['country_code']
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return "{} {} ({}-{})".format(
            self.country, self.region, self.country_code, self.region_code)



class SchoolHolidays(models.Model):
    """Model for school holidays for different years and locations"""
    NRW = 'DE-NW'
    NDS = 'DE-NI'
    COUNTRY_CHOICES = (
        ('DE-BW', 'Baden-Württemberg'),
        ('DE-BY', 'Bayern'),
        ('DE-BE', 'Berlin'),
        ('DE-BB', 'Brandenburg'),
        ('DE-HB', 'Bremen'),
        ('DE-HH', 'Hamburg'),
        ('DE-HE', 'Hessen'),
        ('DE-MV', 'Mecklenburg-Vorpommern'),
        (NDS, 'Niedersachsen'),
        (NRW, 'Nordrhein-Westfalen'),
        ('DE-RP', 'Rheinland-Pfalz'),
        ('DE-SL', 'Saarland'),
        ('DE-SN', 'Sachsen'),
        ('DE-ST', 'Sachsen-Anhalt'),
        ('DE-SH', 'Schleswig-Holstein'),
        ('DE-TH', 'Thüringen'),
    )
    SF = 'SF'
    HOLIDAY_CHOICES = (
        ('OF', 'Osterferien'),
        ('PF', 'Pfingstferien'),
        ('SF', 'Sommerferien'),
        ('HF', 'Herbstferien'),
        ('WF', 'Weihnachtsferien'),
    )

    first_holiday = models.DateField(verbose_name=_("First Holiday"))
    last_holiday = models.DateField(blank=True, null=True,
                                    verbose_name=_("Last Holiday"))
    country = models.CharField(max_length=5, choices=COUNTRY_CHOICES,
                               default=NRW, verbose_name=_("Country"))
    name = models.CharField(max_length=100, choices=HOLIDAY_CHOICES,
                            default=SF, verbose_name=_("Holidays"))

    class Meta:
        ordering = ['first_holiday']
        verbose_name = _('School Holidays')
        verbose_name_plural = _('School Holidays')

    def __str__(self):
        return "{} {}".format(self.get_name_display(), self.first_holiday.year)

    def get_holidays(self):
        first = self.first_holiday
        last = self.last_holiday
        output = [first, ]
        if last:
            output.extend([first + datetime.timedelta(
                days=x) for x in range(0, (last-first).days + 1)])
        return output
