from django.db import models
import string
import random


# Create your models here.
# Create 'fat' models and 'thin' views


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # Room.objects accesses all class objects
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class Room(models.Model):

    # code to enter a room
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)

    # Host of the room and only 1 host per room
    host = models.CharField(max_length=50, unique=True)

    # By default, guest cannot pause
    guest_can_pause = models.BooleanField(null=False, default=False)

    # Number of votes to skip song
    votes_to_skip = models.IntegerField(null=False, default=1)

    # Get the time when room was created
    created_at = models.DateTimeField(auto_now_add=True)
