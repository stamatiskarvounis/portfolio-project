from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    text=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images/")
    
