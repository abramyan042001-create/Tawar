from django.db import models


class Product(models.Model):
    article = models.CharField("Артикул", max_length=50, unique=True)
    name = models.CharField("Наименование", max_length=200)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ("name",)

    def __str__(self):
        return f"{self.article} — {self.name}"
