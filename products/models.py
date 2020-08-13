from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    rank = models.IntegerField()
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='d.jpg')


    def __str__(self):
        return f'{self.name}   price {self.price} rank{self.rank}  date{self.date}'


