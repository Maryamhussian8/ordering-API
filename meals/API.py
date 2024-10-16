from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Meals
from .serializers import MealSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MealsListView(generics.ListAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['name', 'price', 'available']



class MealsDetailView(generics.RetrieveAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer


class MealsCreateView(generics.CreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealsUpdateView(generics.UpdateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer


class MealsDeleteView(generics.DestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer
