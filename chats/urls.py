from django.urls import path
from . import views
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"ws/chats/(?P<room_name>\w+)/$", views.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]