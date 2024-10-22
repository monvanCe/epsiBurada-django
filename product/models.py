from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os
import uuid
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, max_length=254)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def upload_to_product_slug(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('product', instance.product.slug, uuid.uuid4().hex + '.' + ext)

class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to_product_slug)

    def __str__(self):
        imagecount = ProductsImage.objects.filter(product=self.product).count()
        return self.product.slug + imagecount

@receiver(pre_delete, sender=ProductsImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)