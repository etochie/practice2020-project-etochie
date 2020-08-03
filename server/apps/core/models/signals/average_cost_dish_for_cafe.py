from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.core.models import Cafe


@receiver(pre_save, sender=Cafe)
def generate_average_cost_dish(sender, instance, **kwargs):
    """
    Сигнал расчета и сохранения средней стоимости блюд в заведении
    Срабатывает при сохранении модели заведения (pre_save)
    """
    count = instance.dishes.count()
    if count > 0:
        instance.average_cost_dish = instance.get_average_cost_dish()
    else:
        instance.average_cost_dish = 0
