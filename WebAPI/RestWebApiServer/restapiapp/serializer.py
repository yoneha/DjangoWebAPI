# coding: utf-8
from rest_framework import serializers
from .models import User, Entry, SeatInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')

class SeatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatInfo
        fields = ('seatID', 'name', 'attribute', 'status')


from .models import Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('sender', 'title', 'body', 'created_at', 'updated_at', 'lat', 'lng', 'status')