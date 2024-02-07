from django.db import models
import sys

sys.path.insert()

# Create your models here.


class category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_images = models.ImageField(upload_to = "product")

    def __str__ (self):
        return self.category_name
        

class product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_discription = models.TextField(max_length=200)

    def __str__ (self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product_img")
    image = models.ImageField(null=True, blank=True, upload_to = "product")

