from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', null=True)


    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("product:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    condition = models.CharField(max_length=30, null=True, choices=[('new','Jamais utilisé'),('good','Bon état'),('used','Moyen')])
    specs = models.TextField(blank=True)
    desc = models.TextField(blank=True)
    n_price = models.DecimalField(max_digits=8, decimal_places=0)
    r_price = models.DecimalField(max_digits=8, decimal_places=0)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_newproduct = models.BooleanField(default=False)
    userip = models.TextField(default=None, blank=True, null=True)
    visits = models.IntegerField(default=0, null=True)


    class Meta:
        verbose_name_plural= 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.slug])
    


    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 500 or img.width > 500:
            new_img = (700, 700)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/multiimages/")

    def __str__(self):
        return self.product.title


    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 500 or img.width > 500:
            new_img = (800, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path

