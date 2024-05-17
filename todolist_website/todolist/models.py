from django.contrib import admin
from django.db import models

class Task(models.Model):
    # 할일 content
    content = models.CharField(max_length =255)
    #할일 완료여부
    iscompleted = models.BooleanField(default=False)

