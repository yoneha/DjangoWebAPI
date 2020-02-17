from rest_framework import routers
from .views import UserViewSet, EntryViewSet, SeatInfoViewSet, ImageViewSet

# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('entries', EntryViewSet)
# router.register('seatinfo/shinyoko13FS', SeatInfoViewSet)
# router.register('image', ImageViewSet)
# urlpatterns = router.urls

from django.urls import path
from .views import seats_info, sitting_status_info, schedule_info

urlpatterns = [
    path('seatinfo/shinyoko13FS', seats_info),
    path('sittingstatus/<str:id>', sitting_status_info),
    path('schedule/<str:id>', schedule_info),
]
