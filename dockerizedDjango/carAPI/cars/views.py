from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cars
from .serializers import CarsModelSerializer


# Create your views here.

class CarGETView(APIView):

    def get(self, request):
        model = Cars.objects.all()

        serializer = CarsModelSerializer(model, many=True)

        return Response(serializer.data)


class CarPOSTView(APIView):

    def post(self, request):
        serializer = CarsModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarDETAILView(APIView):

    def get(self, request, cars_id):
        cars = Cars.objects.filter(id=cars_id).first()

        if not cars:
            return Response({"Meassage": "Car was not found!"})

        serializer = CarsModelSerializer(cars)

        return Response(serializer.data)

    def delete(self, request, cars_id):

        cars = Cars.objects.filter(id=cars_id).first()

        if not cars:
            return Response({"Message": "The car was not found"}, status=status.HTTP_404_NOT_FOUND)

        cars.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)