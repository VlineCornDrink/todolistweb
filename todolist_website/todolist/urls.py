# todolist/urls.py
from django.urls import path
from . import views


urlpatterns = [
    #views.py파일에서 index함수 요청시 실행
    path('', views.index, name="index"),
    # HTML form 의 action 속성 중 create POST 와 연결 요청시 실행
    path('create_task',views.create_task,name="create_task"),
    # HTML form 의 action 속성 중 GET 와 연결 요청시 실행
    path('delete_task',views.delete_task,name="delete_task"),
    # HTML form 의 action 속성 중 complete POST 와 연결 요청시 실행
    path('complete_task',views.complete_task,name="complete_task"),
]


