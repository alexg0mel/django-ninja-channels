from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=128
    )

    full_name = models.CharField(
        _('Fullname'),
        max_length=128
    )

    numcode = models.PositiveSmallIntegerField(
        _('digital code of country'),
        unique=True,

    )

    alfa3 = models.CharField(
        _('Alfa 3 code'),
        max_length=3,
        unique=True
    )

    alfa2 = models.CharField(
        _('Alfa 2 code'),
        max_length=2,
        unique=True
    )

    sort = models.SmallIntegerField(
        _('Sorting'),
        default=500
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Counties')
        ordering = ('sort', 'alfa3')

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=128
    )

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        related_name='regions',
    )

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        ordering = ('name',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=64
    )

    shortname = models.CharField(
        _('Short name'),
        max_length=4,
        blank=True,
        null=True
    )

    region = models.ForeignKey(
        'Region',
        on_delete=models.CASCADE,
        related_name='cities',
    )

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ('name',)

    def __str__(self):
        return self.name
