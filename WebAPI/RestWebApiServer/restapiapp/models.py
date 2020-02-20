from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField(max_length=200)
    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__  # __str__にも同じ関数を適用


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)

class SeatInfo(models.Model):
    STATUS_SEAT = "seat"
    STATUS_MEETING = "meetingroom"
    ATTRIBUTE_SET = ((STATUS_SEAT, "seat"), (STATUS_MEETING, "meetingroom"))

    STATUS_ATTEND = "Attend"
    STATUS_ABSENT = "Absent"
    STATUS_FREE = "Free"
    STATUS_SET = ((STATUS_ATTEND, "Attend"), (STATUS_ABSENT, "Absent"), (STATUS_FREE, "Free"))
    
    seatID = models.CharField(max_length=50) #ToDo: 一意なキーとする必要あり
    name = models.CharField(max_length=100)
    attribute = models.CharField(choices=ATTRIBUTE_SET, default=STATUS_SEAT, max_length=50)
    status = models.CharField(choices=STATUS_SET, default=STATUS_SEAT, max_length=50)

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')


class Image(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "published"
    STATUS_SET = (
            (STATUS_DRAFT, "draft"),
            (STATUS_PUBLIC, "published"),
    )
    filepath = models.CharField(primary_key=True, max_length=1024)
    sender = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lat = models.FloatField(default=34.75)
    lng = models.FloatField(default=135.5)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.filepath, self.sender, self.title, self.body, self.created_at, self.updated_at, self.lat, self.lng, self.status)