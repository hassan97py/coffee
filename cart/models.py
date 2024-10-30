from django.db import models

# Create your models here.
from django.db import models

class Cart(models.Model):
    items = models.JSONField()  # یا می‌توانید از یک مدل دیگر استفاده کنید


from django.db import models

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name