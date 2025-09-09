from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1.0 or value > 5.0 :
        raise ValidationError("Rating should be within 1 - 5 range.")

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('jacket', 'Jacket'),
    ]
    
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField()
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[validate_rating])
    stock = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    @property
    def is_popular(self):
        return self.purchase_count > 500
    
    @property
    def is_recommended(self):
        return self.purchase_count > 500 and self.rating >= 4.9
    
        
    def increment_buy(self):
        self.purchase_count += 1
        self.save()