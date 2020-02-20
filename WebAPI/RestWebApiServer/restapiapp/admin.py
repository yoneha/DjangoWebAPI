from django.contrib import admin

from .models import User, Entry, SeatInfo, Image, ImageModel, SeikaHappyouCnt


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass

@admin.register(SeatInfo)
class Entry(admin.ModelAdmin):
    pass

@admin.register(Image)
class Entry(admin.ModelAdmin):
    pass

@admin.register(ImageModel)
class Entry(admin.ModelAdmin):
    pass

@admin.register(SeikaHappyouCnt)
class Entry(admin.ModelAdmin):
    pass