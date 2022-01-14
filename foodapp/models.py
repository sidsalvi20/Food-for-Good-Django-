from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Food(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=300)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_cuisine = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    item_taste = models.CharField(max_length=200)
    item_ingredients = models.CharField(max_length=500)
    item_option = models.CharField(max_length=30)
    item_image = models.CharField(max_length=700)



class Comment(models.Model):
    
    text = models.TextField()
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='comments')  
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')

class Profile(models.Model):
    
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')
    person = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.person.username} Profile'
    
    
    
