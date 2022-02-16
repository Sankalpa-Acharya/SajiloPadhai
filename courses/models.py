from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.
class User(AbstractUser):
    gender=models.CharField(max_length=6, choices=[('male','Male'),('female','Female')],default='Male')


    

class Course(models.Model):
    name=models.CharField(max_length=100)
    image=CloudinaryField()
    description=models.CharField(max_length=300)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    
    

# name pass gardini ani redirect hanni 
class Video(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    link=models.CharField(max_length=50)
    description=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    username=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)
    gender=models.CharField(max_length=6,choices=[('female','female'),('male','male')],null=True)
    video=models.ForeignKey(Video,on_delete=models.CASCADE)


    def __str__(self):
        return self.username
    