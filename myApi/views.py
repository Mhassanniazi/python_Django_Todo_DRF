from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import todoSerializer
from todo.models import todoDataSet
# Create your views here.

# this decorator function will decorate the view with GET and POST input entries
@api_view(['GET','POST']) 
def apiView(request):
    if request.method == 'GET':
        allData = todoDataSet.objects.all()
        # here we are serializing the model list of instances that'swhy used many=True
        serializerr = todoSerializer(allData,many=True)
        # returning serialized data to the frontend
        return Response(serializerr.data)
    elif request.method == "POST":
        print("DATA IS: ",request.data,"and",type(request.data))
        print("DATATATTTA IS: ",request.POST)
        # request.data me woh object ajaega(in dict) jo hum bhejengay on post request
        # yaha request.data me deserialized data aya usko humnay save kerdia
        serializerr = todoSerializer(data=request.data)
        if serializerr.is_valid():
            serializerr.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializerr.errors,status = status.HTTP_400_BAD_REQUEST)

# links
# https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c