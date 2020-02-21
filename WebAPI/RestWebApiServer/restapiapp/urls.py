from rest_framework import routers
from .views import UserViewSet, EntryViewSet, SeatInfoViewSet, ImageViewSet

# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('entries', EntryViewSet)
# router.register('seatinfo/shinyoko13FS', SeatInfoViewSet)
# router.register('image', ImageViewSet)
# urlpatterns = router.urls

from django.urls import path
from .views import seats_info, sitting_status_info, schedule_info, upload_img
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('seatinfo/shinyoko13FS', seats_info),
    path('sittingstatus', sitting_status_info),
    path('schedule', schedule_info),
    # path('uploadImg', upload_img),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #開発用コード 画像ファイルの扱い
