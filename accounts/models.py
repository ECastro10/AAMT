from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def member_upload_handler(instance, filename):
    return '{username}/img/{filename}'.format(username=instance.username, filename=filename)

class Member(AbstractUser):

    bio = models.TextField(blank=True, null=True)
    instruments = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=member_upload_handler, blank=True, null=True)
    lessons_completed = []


    def __str__(self):
        return self.username

class Instrument(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    member = models.ForeignKey('Member')


class Lesson(models.Model):

    lesson_name = models.CharField(max_length=255, blank=True, null=True)
    member = Member.objects.all()
