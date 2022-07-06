from django.core.validators import MaxValueValidator
from django.db import models


class ColorsChoices(models.TextChoices):
    BLACK = 'black', 'Black'
    WHITE = 'white', 'White'
    RED = 'red', 'Red'


class Color(models.Model):
    name = models.CharField("Color", help_text='Name of color', max_length=200)

    def __str__(self) -> str:
        return f'{self.name}'

    __repr__ = __str__


class Human(models.Model):
    name = models.CharField("Name", help_text='It is name human', max_length=200)
    age = models.PositiveIntegerField("Age", help_text="How old this human", validators=[MaxValueValidator(150)])

    favourite_color = models.CharField(
        'Favorite color',
        max_length=32,
        choices=ColorsChoices.choices,
        default=ColorsChoices.WHITE
    )

    favorite_color_by_foreign_key = models.ForeignKey(
        Color,
        related_name='humans_related_by_foreign_key',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    favorite_color_many_to_many = models.ManyToManyField(
        Color,
        related_name='humans_related_by_many_to_many',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.age}'

    __repr__ = __str__

    # def __repr__(self) -> str:
    #     return
