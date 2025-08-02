from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product( models.Model ):
    category_choices = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('undefined', 'Undefined'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True, null=True)
    category = models.CharField(choices=category_choices, default='undefined', max_length=20)

    # models.py (inside Product)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
          return round(sum(r.rating for r in reviews) / reviews.count(), 1)
          return 0
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"

class pro_gallery( models.Model ):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='gallery')
    image = models.ImageField(upload_to='gallery/%y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f"Gallery for {self.product.name}"
    
    class Meta:
        verbose_name_plural = "Product Gallery"

class product_review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'product')  # ✅ matches field name exactly

    def __str__(self):
        return f"{self.user.username} review on {self.product.name}"


    


