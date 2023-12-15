from django.db import models

class Train(models.Model):
    Train_Name=models.CharField(max_length=250)
  #  Origin=models.ForeignKey(,on_delete=models.CASCADE)
    Destination=models.CharField(max_length=250)
    Date_Of_Departure=models.DateField()
    Return_Of_Departure=models.DateField()

    class Meta:
        verbose_name="Kelassor Train"
    def __str__(self) -> str:
        return "{}-{}-{}".format (self.Train_Name,self.Origin,self.Destination)


# class station(models.Model):
#     name=models.CharField(max_length=250)    


