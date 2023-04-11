from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        "category.Category",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
