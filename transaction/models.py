from django.db import models


class Transaction(models.Model):
    item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    buyer = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.buyer}"

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["-date"]