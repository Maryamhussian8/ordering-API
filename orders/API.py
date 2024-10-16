from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework.response import Response
from rest_framework import status

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'status', 'total_price']  
    ordering_fields = ['total_price', 'created_at']


class OrderDetaiAPIlView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=self.request.user)  
            total_price = 0
            for item_data in request.data.get('items', []):
                item_serializer = OrderItemSerializer(data=item_data)
                if item_serializer.is_valid():
                    order_item = item_serializer.save(order=order)
                    total_price += order_item.meal.price * order_item.quantity

            order.total_price = total_price
            order.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer