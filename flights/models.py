from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    # duration=models.IntegerField()

    def __str__(self):
        return  f"Flight fromm {self.origin} to {self.destination}"



# drf __str__ reprsents a string representation of a 
#Foreing key -one to many, referenec to another table

#inside we can shell insert the datas, python3 manage.py shell tehn print