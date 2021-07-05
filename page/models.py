from django.db import models

# Create your models here.
class User_data(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    date=models.DateField()
    number=models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.name,self.email)


class Anthologies(models.Model):
    anthology_name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='anthology')

    def __str__(self):
        return self.anthology_name


