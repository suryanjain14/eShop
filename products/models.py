from django.db import models


# Create your models here.
class Products(models.Model):
    category_choice = [("agriculture_power_sprayer", "agriculture_power_sprayer"),
                       ("air_& vacuum pump", "air & vacuum pump"), ("car washers", "car washers"),
                       ("compressor", "compressor"), ("electric motors", "electric motors"), ("foam gun", "foam gun"),
                       ("foam tank", "foam tank"),
                       ("garage equipment & accessories", "garage equipment & accessories"),
                       ("grease pump", "grease pump"), ("hi-pressure pump & pipe", "hi-pressure pump & pipe"),
                       ("impact wrench", "impact wrench"), ("pneumatic fitting", "pneumatic fitting"),
                       ("spray gun", "spray gun"), ("tire inflating gun", "tire inflating gun"),
                       ("vacuum cleaners", "vacuum cleaners"), ("welding machine", "welding machine"),
                       ("agriculture sprayer parts", "agriculture sprayer parts"), ("hardware_items", "hardware_items")]
    name = models.CharField(max_length=40)
    price = models.FloatField()
    rank = models.IntegerField(unique=True)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='d.jpg',upload_to='media/profile',unique=True)
    Category = models.CharField(max_length=40, choices=category_choice,default='compressor')

    def __str__(self):
        return f'{self.name}   price {self.price} rank{self.rank}  date{self.date}'
