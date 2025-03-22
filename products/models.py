from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Product Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Category")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    ingredients = models.TextField(verbose_name="Ingredients")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True ,default='product_images/default.jpg') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
