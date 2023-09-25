from django.db import models
from core.models import BaseModel, Person, Project


class Room(BaseModel):
    name = models.CharField(max_length=144, null=True)
    description = models.TextField(null=True)
    members = models.ManyToManyField(Person)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=144, null=True, choices=(('private', 'private'), ('public', 'public')))

    def __str__(self):
        return self.name

class Message(BaseModel):
    content = models.TextField(null=True)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sender.user.username