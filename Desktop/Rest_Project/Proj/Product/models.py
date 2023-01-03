from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    product_elements = models.ForeignKey("Elements", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Elements(models.Model):
    element_id = models.ManyToManyField("Product")


class Category(models.Model):
    cat_id = models.IntegerField(unique=True, primary_key=True)


class Likes(models.Model):
    like_id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)



class Comments(models.Model):
    com_id = models.IntegerField(unique=True, primary_key=True)
    product = models.ManyToManyField("Product")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
