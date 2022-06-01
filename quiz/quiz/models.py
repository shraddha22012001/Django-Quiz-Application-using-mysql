from django.db import models

class Exam(models.Model):    
    ID = models.AutoField(primary_key=True) 
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=300)
    Option2 = models.CharField(max_length=300)
    Option3 = models.CharField(max_length=300)
    Option4 = models.CharField(max_length=300)
    Correctans = models.CharField(max_length=300)
    class Meta:  
        db_table = "onlineexam" 