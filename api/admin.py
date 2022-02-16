from django.contrib import admin

from api.models import Task

# Register your models here.
from . models import Task

admin.site.register(Task)
