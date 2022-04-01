from django.db import models
from django.contrib.auth.models import User




class product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name


