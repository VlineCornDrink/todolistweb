from django.contrib import admin
from .models import Task

# Register your models here.
# todolist/admin.py

#models.py함수에 있는 task table 관리자 페이지에 등록
admin.site.register(Task)

