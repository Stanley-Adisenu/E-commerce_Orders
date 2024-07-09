from django.contrib import admin
from .models import OrderItems,Orders,User

# Register your models here.
# admin.site.register(Status)
admin.site.register(OrderItems)
admin.site.register(Orders)
admin.site.register(User)



