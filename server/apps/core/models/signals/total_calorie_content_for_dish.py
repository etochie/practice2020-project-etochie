from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.core.models import Dish


@receiver(m2m_changed, sender=Dish.ingredients.through)
def generate_total_calorie_content(sender, instance, **kwargs):
    """
    Сигнал расчета и сохранения калорийности блюда.
    Срабатывает при изменении отношений моделей блюд и ингредиентов.
    Вызывает сохранение модели блюда и модели заведения, в котором есть это блюдо.
    """
    count = instance.ingredients.count()
    if count > 0:
        instance.total_calorie_content = instance.get_total_calorie_content()
        instance.save()
        instance.cafe.save()
