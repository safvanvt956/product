from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    parshapa = models.CharField(max_length=100)
    image = models.ImageField()
    slue = models.SlugField(max_length=100)


    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Category")


    def __str__(self):
        return self.title
    

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    slue = models.SlugField(max_length=100)
    parshapa = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = ("Subcategory")
        verbose_name_plural = ("Subcategory")

    def __str__(self):
        return self.title

  
class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.FloatField()
    oldprice = models.FloatField()
    subcategory = models.ForeignKey("product.Subcategory", on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title
    




    

  
