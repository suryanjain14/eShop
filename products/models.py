from django.db import models


# Create your models here.
class Products(models.Model):
    category_choice = [("AGRICULTURE POWER SPRAYER", "AGRICULTURE POWER SPRAYER"),
                       ("AIR_& VACUUM PUMP", "AIR & VACUUM PUMP"), ("CAR WASHERS", "CAR WASHERS"),
                       ("COMPRESSOR", "COMPRESSOR"), ("ELECTRIC MOTORS", "ELECTRIC MOTORS"), ("FOAM GUN", "FOAM GUN"),
                       ("FOAM TANK", "FOAM TANK"),
                       ("GARAGE EQUIPMENT & ACCESSORIES", "GARAGE EQUIPMENT & ACCESSORIES"),
                       ("GREASE PUMP", "GREASE PUMP"), ("HI-PRESSURE PUMP & PIPE", "HI-PRESSURE PUMP & PIPE"),
                       ("IMPACT WRENCH", "IMPACT WRENCH"), ("PNEUMATIC FITTING", "PNEUMATIC FITTING"),
                       ("SPRAY GUN", "SPRAY GUN"), ("TIRE INFLATING GUN", "TIRE INFLATING GUN"),
                       ("VACUUM CLEANERS", "VACUUM CLEANERS"), ("WELDING MACHINE", "WELDING MACHINE"),
                       ("AGRICULTURE SPRAYER PARTS", "AGRICULTURE SPRAYER PARTS"), ("HARDWARE_ITEMS", "HARDWARE_ITEMS")]
    name = models.CharField(max_length=40)
    price = models.FloatField()
    rank = models.IntegerField(unique=True)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='d.jpg',upload_to='profile',unique=True)
    Category = models.CharField(max_length=40, choices=category_choice,default='compressor')

    def __str__(self):
        return f'{self.name}   price:{self.price} rank:{self.rank}  date:{self.date}  category:{self.Category}'
