from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extends the AbstractUser to contain user balance
    """
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=100.00)


class Trade(models.Model):
    """
    Trade model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profit_or_loss = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.user.username}'
