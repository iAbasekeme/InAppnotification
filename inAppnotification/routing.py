from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^(?P<room_name>[^/]+)/$', consumers.NotificationConsumer.as_asgi()),
]