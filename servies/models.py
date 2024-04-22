from django.db import models

from PIL import Image

# Create your models here.
class Servies(models.Model):
    servies_icon=models.FileField(upload_to="project/", max_length=300,null=True,default=None)
    servies_title=models.CharField(max_length=50)
    servies_des = models.TextField()
    servies_git_url = models.CharField(max_length=150,null=True,default=None)
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        image = Image.open(self.servies_icon.path)
         # Set the desired width and height
        desired_width = 360
        desired_height = 170
        
        image = image.resize((desired_width, desired_height), Image.ANTIALIAS)
        image.save(self.servies_icon.path)

class ContectUs(models.Model):
    user_name = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=15)
    user_email = models.EmailField(max_length=70,unique=True)
    user_message = models.CharField(max_length=200) 