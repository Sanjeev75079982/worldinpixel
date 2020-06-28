from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    # description = models.TextField()



    class Meta:
        verbose_name =  'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


#create image model

class Image(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_date']



class Subscription(models.Model):
    
    sub_type = models.CharField(max_length=50,null=True)
    price = models.IntegerField()
    
    
    
    def __str__(self):
        return str(self.price)







class UserForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
   

    
    

    
    def __str__(self):
        return self.user.username














    



    
        


    
