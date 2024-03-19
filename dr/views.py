from django.shortcuts import render

from rest_framework.decorators import api_view
# Create your views here.

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q


from . import models,serializers

@api_view(["GET","POST"])
def drink_list(request):
   
   if request.method=="GET":
       drinks=models.Drink.objects.all()
       serializer=serializers.drinkSerializer(drinks,many=True)
       print(serializer)
       return JsonResponse({"drink":serializer.data},safe=False)
   elif request.method=="POST":
       serializer=serializers.drinkSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(["GET","PUT","DELETE"])
def drink_details(request,id):
    try:
        drink=models.Drink.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=="GET":
      serializer=serializers.drinkSerializer(drink)
      return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer=serializers.drinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=="DELETE":
        drink.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def drink_search(request):
    if request.method=="GET":
        search_query=request.query_params.get("q","")
        drinks=models.Drink.objects.filter(
            Q(name__icontains=search_query)|Q(decription__icontains=search_query)
        )
        drink_serializer=serializers.drinkSerializer(drinks,many=True)

        return Response(drink_serializer.data)
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)