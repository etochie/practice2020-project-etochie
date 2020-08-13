from django.db import models
from rest_framework.exceptions import APIException
from yandex_geocoder import Client

from config.settings.api_keys import YANDEX_GEOCODER_KEY


class Cafe(models.Model):
    """Модель заведения"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название заведения',
        help_text='Введите название заведения'
    )
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография заведения',
        upload_to='cafe_photos',
        help_text='Загрузите фотографию заведения'
    )
    open_hour = models.IntegerField(
        verbose_name='Время открытия',
        help_text='Введите время открытия заведения'
    )
    close_hour = models.IntegerField(
        verbose_name='Время закрытия',
        help_text='Введите время закрытия заведения'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес заведения',
        help_text='Введите адрес заведения. Координаты сгенерируются автоматически.'
    )
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
        verbose_name='Владелец заведения',
        related_name='cafes'
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

    def get_average_cost_dish(self):
        """
        Возвращает среднюю стоимость всех блюд заведения.
        Используется в сигнале average_cost_dish_for_cafe.
        """
        if self.dishes:
            total = 0
            values = self.dishes.values()
            count = self.dishes.count()
            for obj in values:
                total += obj['price']
            try:
                average = total / count
            except ZeroDivisionError:
                average = 0
            return average

    def save(self, *args, **kwargs):
        """Переопределение метода save для сохранения координат"""
        if self.address:
            coords = self.get_coords()
            self.coordinates_longitude = coords[0]
            self.coordinates_latitude = coords[1]
        super(Cafe, self).save(*args, **kwargs)


class Dish(models.Model):
    """Модель блюда"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название блюда',
        help_text='Введите название блюда'
    )
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name='dishes',
        help_text='Выберете заведение, к которому будет привязано это блюдо'
    )
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография блюда',
        upload_to='dish_photos',
        help_text='Загрузите фотографию блюда'
    )
    total_calorie_content = models.IntegerField(
        default=0,
        verbose_name='Суммарная калорийность блюда'
    )
    price = models.IntegerField(
        verbose_name='Цена блюда',
        help_text='Введите цену блюда'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        verbose_name='Ингредиенты блюда',
        blank=True,
        help_text='Выберете ингредиенты блюда из списка'
    )

    def __str__(self):
        return self.name

    def get_total_calorie_content(self):
        """
        Возвращает суммарную калорийность блюда на 100 грамм.
        Используется в сигнале total_calorie_content_for_dish.
        """
        if self.ingredients:
            temp = 0
            values = self.ingredients.values()
            count = self.ingredients.count()
            for obj in values:
                temp += obj['calorie_content']
            try:
                calories = temp / count
            except ZeroDivisionError:
                calories = 0
            return calories


class Ingredient(models.Model):
    """Модель ингредиента"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название ингредиента'
    )
    calorie_content = models.IntegerField(
        default=0,
        verbose_name='Калорийность ингредиента'
    )

    def __str__(self):
        return self.name
