from django.db import models


# Create your models here.
class Message(models.Model):

    message = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name:{self.name} time{self.time}'


