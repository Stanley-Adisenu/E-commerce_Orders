from django.urls import path,include
from . import views

urlpatterns = [
    # path('status/', views.status_list),
    path('orders/', views.order_list),

    path('orders/<int:pk>/', views.order_update),

    path('orderitems/', views.order_items_list),
    
    path('myorders/<int:pk>/', views.user_orders),
]