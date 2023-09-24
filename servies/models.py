from django.db import models

# Create your models here.
class Servies(models.Model):
    servies_icon=models.FileField(upload_to="project/", max_length=300,null=True,default=None)
    servies_title=models.CharField(max_length=50)
    servies_des = models.TextField()
    servies_git_url = models.CharField(max_length=150,null=True,default=None)