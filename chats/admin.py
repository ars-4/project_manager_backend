from django.contrib import admin
from chats.models import Room, Message
# Register your models here.

REGISTERED_MODELS = [
    Room,
    Message
]

admin.site.register(REGISTERED_MODELS)
