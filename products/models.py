from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    # Make category nullable to avoid issues with existing rows or provide a default id
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    # Use default instead of auto_now_add
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['created_at']),
        ]
