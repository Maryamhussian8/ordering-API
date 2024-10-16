from django.urls import path
from .API import OrderListAPIView, OrderCreateAPIView, OrderUpdateAPIView, OrderDeleteAPIView

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='order_list'),
    path('create/', OrderCreateAPIView.as_view(), name='create_order'),
    path('update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteAPIView.as_view(), name='order_delete'),
    
]
