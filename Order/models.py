from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField( max_length=500)

    def __str__(self):
        return self.name
    
    

class Orders(models.Model):
    STATUS_CHOICES = (
    ('created', 'created'),
    ('processing', 'processing'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    total_amount = models.FloatField()
    status =  models.CharField(choices=STATUS_CHOICES, default="created",max_length=15)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at =models.DateTimeField(auto_now=True,null=True,blank=True)


class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    listings = models.CharField(max_length=500)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
