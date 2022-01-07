from django.conf import settings
from django.db import models


class Services(models.Model):
    "Generated Model"
    price = models.FloatField()
    commission = models.IntegerField()
    client = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="services_client",
    )
    details = models.TextField()


# Create your models here.
