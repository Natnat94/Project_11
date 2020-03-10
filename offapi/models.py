from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# This models create the database based on the OFF api data ready to be populate


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Store(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    link = models.TextField(null=True)
    description = models.TextField(null=True)
    nutriscore = models.CharField(max_length=2)
    mini_image = models.TextField(null=True)
    image = models.TextField(null=True)
    nutriments = models.TextField(null=True)
    stores = models.ManyToManyField(Store, related_name="productes")

    def __str__(self):
        return self.product_name


class ProductSaved(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="+"
    )
    sub_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="+"
    )

    def __str__(self):
        return "%s - %s" % (self.user_id, self.product_id)

    class Meta:
        verbose_name_plural = "Product saved"
