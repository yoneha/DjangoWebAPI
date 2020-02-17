# coding: utf-8
import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, SeatInfo
from .serializer import UserSerializer, EntrySerializer, SeatInfoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class SeatInfoViewSet(viewsets.ModelViewSet):
    queryset = SeatInfo.objects.all()
    serializer_class = SeatInfoSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def seats_info(request):
  
  # post = SeatInfo.objects.filter(seatID='0001')
  items = SeatInfo.objects.all()

  json = {
    "updatetime" : "1570242891",
    "seats" :
    [
      {
        "id": items[0].seatID,
        "name": items[0].name,
        "attribute": items[0].attribute
      },
      {
        "id": items[1].seatID,
        "name": items[1].name,
        "attribute": items[1].attribute
      },
      {
        "id": items[2].seatID,
        "name": items[2].name,
        "attribute": items[2].attribute
      },
      {
        "id": items[3].seatID,
        "name": items[3].name,
        "attribute": items[3].attribute
      },
    ]
  }
  
  return Response(json)

@api_view(['GET'])
def sitting_status_info(request, id):
  
  post = SeatInfo.objects.filter(seatID=id)

  json = {
    "updatetime" : "1570242891",
    "state" : post[0].status,
  }

  return Response(json)

@api_view(['GET'])
def schedule_info(request, id):
  json = {
	  "schedules" : 
    [
      {
        "starttime": "2020-02-13T17:30:00.0000000",
        "endtime": "2020-02-13T19:30:00.0000000",
        "subject": "UTレビュー"
      },
  		{
        "starttime": "2020-02-13T13:30:00.0000000",
        "endtime": "2020-02-13T14:30:00.0000000",
        "subject": "UTレビュー"
      }
  	]
  }
  return Response(json)






from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
# from rest_framework.decorators import detail_route, list_route
import os
from rest_framework.response import Response

from .models import Image
from .serializer import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
  UPLOAD_DIR = '../statics/uploaded_photo/'
  queryset = Image.objects.all()
  serializer_class = ImageSerializer

def create(self, request):
    file = request.FILES['file']
    path = os.path.join(UPLOAD_DIR, file.name)
    destination = open(path, 'wb')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    if not os.path.exists(path):
        print('File not found:', path)
        return create_render(request)

    image, created = Image.objects.get_or_create(filepath=path)
    if created:
        # image.sender = request.POST['sender']
        image.title = request.POST['title']
        image.body = request.POST['body']
        image.created_at = request.POST['created_at']
        image.updated_at = request.POST['updated_at']
        image.lat = float(request.POST['lat'])
        image.lng = float(request.POST['lng'])
        image.status = request.POST['status']
        image.save()

    return Response({'message': 'OK'})