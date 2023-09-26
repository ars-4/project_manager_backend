from django.shortcuts import render
import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from django.http import HttpResponse
from .models import Room, Person, Message
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chats.serializers import RoomSerializer, MessageSerializer

def index(request):
    return render(request, "chats/index.html")

def room(request, room_name):
    return render(request, "chats/room.html", {"room_name": room_name})

@api_view(['GET'])
def rooms_by_project(request, pk):
    rooms = Room.objects.filter(project=pk)
    serializer = RoomSerializer(rooms, many=True)
    return Response({"rooms": serializer.data}, status=200)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        available_rooms = await sync_to_async(list)(Room.objects.all())

        if self.room_name not in [room.name for room in available_rooms]:
            self.close(code=404)
            return HttpResponse("Room not found", status=404)
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        token = text_data_json["token"]
        user = 'Anonymous'
        timestamp = str(datetime.datetime.now()).split(".")[0]

        can_user_message = False
        tokens = await database_sync_to_async(Token.objects.all, thread_sensitive=True)()
        for available_token in tokens:
            if available_token.key == token:
                user = available_token.user
                can_user_message = True

        if not can_user_message:
            self.close(code=403)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, 'user': user.username, 'token': token, 'timestamp': timestamp}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        token = event["token"]
        timestamp = str(datetime.datetime.now()).split(".")[0]

        user = 'Anonymous'

        tokens = await database_sync_to_async(Token.objects.all, thread_sensitive=True)()
        for available_token in tokens:
            if available_token.key == token:
                user = available_token.user

        persons = await database_sync_to_async(Person.objects.all, thread_sensitive=True)()

        can_user_message = False
        for person in persons:
            if person.user == user:
                can_user_message = True
        
        if not can_user_message:
            self.close(code=403)
        

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'user': user.username, 'token': token, 'timestamp': timestamp}))