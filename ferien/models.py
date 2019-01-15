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
    region = models.CharField(max_length=100, blank=True,
                              verbose_name=_("Region"))
    iso = models.CharField(max_length=6, blank=True, verbose_name=_("ISO Code"))
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
    country = models.ForeignKey(Country, default=1, on_delete=models.CASCADE,
                                verbose_name=_("Country"))
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
