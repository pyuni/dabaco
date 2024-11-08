from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class contactClass(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    msg=models.CharField(max_length=400)
    def __str__(self):
        return self.firstname

class staticContentClass(models.Model):
    key=models.CharField(max_length=10)
    txt=RichTextField()
    title=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.key

class categoryClass(models.Model):
    title=models.CharField(max_length=30)
    img=models.ImageField(upload_to="photo")
    description=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

class serviceClass(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(categoryClass,on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self):
        return self.title
    
class homePage(models.Model):
    img=models.ImageField(upload_to="photo")
    txt1=models.CharField(max_length=50)
    txt2=models.CharField(max_length=50)
    txt3=models.CharField(max_length=50)