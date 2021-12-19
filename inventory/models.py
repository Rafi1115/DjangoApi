from django.db import models



class Supplier(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='2. Suppliers'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=200)
    note = models.TextField(blank=False)
    image = models.ImageField(upload_to='product/images', blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, related_name='suppliers', on_delete=models.CASCADE)
 
    class Meta:
        verbose_name_plural='1. Products'

    def __str__(self):
        return self.name

    @property
    def supplier_name(self):
        return self.supplier.name

        