# coding: utf-8
import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, SeatInfo, SeikaHappyouCnt
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
from django.shortcuts import render
import json



def upload_img(request):
  cnt = SeikaHappyouCnt.objects.get(pk=1)
  item3 = SeatInfo.objects.get(seatID='seat-0100003')
  item4 = SeatInfo.objects.get(seatID='seat-0100004')
  item5 = SeatInfo.objects.get(seatID='seat-0100005')
  item6 = SeatInfo.objects.get(seatID='seat-0100006')
  if request.method == 'POST':
    if cnt.count % 4 == 0:
      item3.status = "Free"
      item4.status = "Free"
      item5.status = "Free"
      item6.status = "Free"
      item3.save()    
      item4.save()    
      item5.save()    
      item6.save()    
    elif cnt.count % 4 == 1:
      item3.status = "Absent"
      item4.status = "Absent"
      item5.status = "Absent"
      item6.status = "Absent"
      item3.save()    
      item4.save()    
      item5.save()    
      item6.save()    
    elif cnt.count % 4 == 2:
      item3.status = "Attend"
      item4.status = "Attend"
      item5.status = "Attend"
      item6.status = "Attend"
      item3.save()    
      item4.save()    
      item5.save()    
      item6.save()  
    elif cnt.count % 4 == 3:
      item3.status = "Attend"
      item4.status = "Absent"
      item5.status = "Attend"
      item6.status = "Absent"
      item3.save()    
      item4.save()    
      item5.save()    
      item6.save()  
    cnt.count += 1
    cnt.save()
    print (cnt.count)

  # else:
  #       items.status = "Absent"
  #   items.save()

  return render(request, 'upload_img.html',)


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
      {
        "id": items[4].seatID,
        "name": items[4].name,
        "attribute": items[4].attribute
      },
      {
        "id": items[5].seatID,
        "name": items[5].name,
        "attribute": items[5].attribute
      },
      {
        "id": items[6].seatID,
        "name": items[6].name,
        "attribute": items[6].attribute
      },
      {
        "id": items[7].seatID,
        "name": items[7].name,
        "attribute": items[7].attribute
      },
      {
        "id": items[8].seatID,
        "name": items[8].name,
        "attribute": items[8].attribute
      },
      {
        "id": items[9].seatID,
        "name": items[9].name,
        "attribute": items[9].attribute
      },
      {
        "id": items[10].seatID,
        "name": items[10].name,
        "attribute": items[10].attribute
      },
      {
        "id": items[11].seatID,
        "name": items[11].name,
        "attribute": items[11].attribute
      },
    ]
  }
  
  return Response(json)

@api_view(['GET'])
def sitting_status_info(request):
  
  # post = SeatInfo.objects.filter(seatID=id)
  items = SeatInfo.objects.all()
  
  json = {
    "status":
    [
      {
        "id": items[0].seatID,
        "updatetime": "1570242891",
        "state": items[0].status
      },
      {
        "id": items[1].seatID,
        "updatetime": "1570242891",
        "state": items[1].status
      },
      {
        "id": items[2].seatID,
        "updatetime": "1570242891",
        "state": items[2].status
      },
      {
        "id": items[3].seatID,
        "updatetime": "1570242891",
        "state": items[3].status
      },
      {
        "id": items[4].seatID,
        "updatetime": "1570242891",
        "state": items[4].status
      },
      {
        "id": items[5].seatID,
        "updatetime": "1570242891",
        "state": items[5].status
      },
      {
        "id": items[6].seatID,
        "updatetime": "1570242891",
        "state": items[6].status
      },
      {
        "id": items[7].seatID,
        "updatetime": "1570242891",
        "state": items[7].status
      },
      {
        "id": items[8].seatID,
        "updatetime": "1570242891",
        "state": items[8].status
      },
      {
        "id": items[9].seatID,
        "updatetime": "1570242891",
        "state": items[9].status
      },
      {
        "id": items[10].seatID,
        "updatetime": "1570242891",
        "state": items[10].status
      },
      {
        "id": items[11].seatID,
        "updatetime": "1570242891",
        "state": items[11].status
      },
    ]
  }

  return Response(json)

@api_view(['GET'])
def schedule_info(request):
  json = {
    "schedules":
    [
      {
        "id": "seat-0100003",
        "schedule": [
          {
            "title": "朝礼オンライン",
            "start": "2020-02-19 08:55:00.000Z",
            "end": "2020-02-19 09:10:00.000Z"
          },
          {
            "title": "【産業ステカメ】デイリーミーティング",
            "start": "2020-02-19 10:00:00.000Z",
            "end": "2020-02-19 10:30:00.000Z"
          },
          {
            "title": "単体テストコードレビュー",
            "start": "2020-02-19 10:30:00.000Z",
            "end": "2020-02-19 11:00:00.000Z"
          },
          {
            "title": "MI-1自動キャリブ定例会",
            "start": "2020-02-19 14:00:00.000Z",
            "end": "2020-02-19 15:00:00.000Z"
          },
          {
            "title": "自己学習時間確保",
            "start": "2020-02-19 15:00:00.000Z",
            "end": "2020-02-19 16:00:00.000Z"
          },
        ]
      },
      {
        "id": "seat-0100004",
        "schedule": [
          {
            "title": "EWT 9:00-17:30",
            "start": "2020-02-19 08:00:00.000Z",
            "end": "2020-02-19 08:30:00.000Z"
          },
          {
            "title": "朝礼オンライン",
            "start": "2020-02-19 08:55:00.000Z",
            "end": "2020-02-19 09:10:00.000Z"
          },
          {
            "title": "LDTRデイリー",
            "start": "2020-02-19 09:30:00.000Z",
            "end": "2020-02-19 10:00:00.000Z"
          },
          {
            "title": "自己学習時間確保",
            "start": "2020-02-19 15:00:00.000Z",
            "end": "2020-02-19 16:00:00.000Z"
          },
          {
            "title": "FW: いきいき活動",
            "start": "2020-02-19 16:00:00.000Z",
            "end": "2020-02-19 16:30:00.000Z"
          },
          {
            "title": "成果発表会会場確認予備",
            "start": "2020-02-19 16:30:00.000Z",
            "end": "2020-02-19 17:30:00.000Z"
          },
        ]
      },
      {
        "id": "seat-0100005",
        "schedule": [
          {
            "title": "EWT(9:00~17:30)",
            "start": "2020-02-19 08:30:00.000Z",
            "end": "2020-02-19 09:00:00.000Z"
          },
          {
            "title": "朝礼オンライン",
            "start": "2020-02-19 08:55:00.000Z",
            "end": "2020-02-19 09:10:00.000Z"
          },
          {
            "title": "【産業ステカメ】デイリーミーティング",
            "start": "2020-02-19 10:00:00.000Z",
            "end": "2020-02-19 10:30:00.000Z"
          },
          {
            "title": "自己学習時間確保",
            "start": "2020-02-19 15:00:00.000Z",
            "end": "2020-02-19 16:00:00.000Z"
          },
        ]
      },
      {
        "id": "seat-0100006",
        "schedule": [
          {
            "title": "朝礼オンライン",
            "start": "2020-02-19 08:55:00.000Z",
            "end": "2020-02-19 09:10:00.000Z"
          },
          {
            "title": "LDTRデイリー",
            "start": "2020-02-19 09:30:00.000Z",
            "end": "2020-02-19 10:00:00.000Z"
          },
          {
            "title": "LFE 現状共有",
            "start": "2020-02-19 14:00:00.000Z",
            "end": "2020-02-19 15:00:00.000Z"
          },
          {
            "title": "自己学習時間確保",
            "start": "2020-02-19 15:00:00.000Z",
            "end": "2020-02-19 16:00:00.000Z"
          },
        ]
      },
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