from django.db import models

class Registration(models.Model):
    account_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
