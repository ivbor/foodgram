from django.db import models


class Ingredient(models.Model):
    """Модель для ингредиентов."""
    name = models.CharField('Название', max_length=128, unique=True)
    measurement_unit = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self):
        return self.name
