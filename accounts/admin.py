from django.contrib import admin
from .models import Member, Instrument, Lesson

# Register your models here.
admin.site.register(Member)
admin.site.register(Instrument)
admin.site.register(Lesson)