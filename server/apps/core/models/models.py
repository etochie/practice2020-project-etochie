from django.db import models
from rest_framework.exceptions import APIException
from yandex_geocoder import Client

from config.settings.api_keys import YANDEX_GEOCODER_KEY


class Cafe(models.Model):
    """Модель заведения"""
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография заведения',
        upload_to='cafe_photos'
    )
    open_hour = models.IntegerField(verbose_name='Время открытия')
    close_hour = models.IntegerField(verbose_name='Время закрытия')
    address = models.CharField(max_length=255, verbose_name='Адрес заведения')
    average_cost_dish = models.IntegerField(
        verbose_name='Средняя стоимость блюд',
        blank=True,
        null=True
    )
    coordinates_longitude = models.DecimalField(
        verbose_name='Координаты долгота',
        max_digits=10,
        decimal_places=7,
        blank=True
    )
    coordinates_latitude = models.DecimalField(
        verbose_name='Координаты широта',
        max_digits=10,
        decimal_places=7,
        blank=True
    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец заведения'
    )

    def __str__(self):
        return self.name

    def get_coords(self):
        """Возвращает координаты заведения (долгота, широта)"""
        client = Client(YANDEX_GEOCODER_KEY)
        try:
            coord = client.coordinates(self.address)
        except Exception:
            raise APIException(
                'Невозможно определить координаты заведения. Проверьте правильность адреса.'
            )
        return coord

    def save(self, *args, **kwargs):
        """Переопределение метода save для сохранения координат"""
        if self.address:
            self.coordinates_longitude = self.get_coords()[0]
            self.coordinates_latitude = self.get_coords()[1]
        super(Cafe, self).save(*args, **kwargs)
