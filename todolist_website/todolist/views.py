# 템플릿 로드
from django.shortcuts import render
# HTTP 응답 생성 및 URL Redirection(다른 URL 자동 이동)
from django.http import HttpResponse,HttpResponseRedirect
# URL 패턴 이름을 이용하여 URL 생성
from django.urls import reverse
# models.py에 정의된 모델 Task 가져오기
from .models import Task #models.py에 있는 Task 함수

# todolist 사이트
def index(request):
     # Task 테이블 데이터 모두 가져오기
     tasks = Task.objects.all()
     # 저장된 할일들 DB에서 가져와 context 딕셔너리 변수에 넣기
     content = {'tasks':tasks}
     
     # todolist/html 템플릿 사용하여 Task 객체 웹페이지에 보여줌
     return render(request,"todolist/index.html",content)
    
# 할일 만드는 task
def create_task(request):
    # 할일
    user_input_create = request.POST['whattodo']
    # 할일 레코드 테이블에 추가
    new_record = Task(content=user_input_create)
    new_record.save()
    # 다시 사이트 불러오기
    return HttpResponseRedirect(reverse('index'))

# 할일 삭제하는 task
def delete_task(request):
    # 삭제할 할일
    user_input_delete = request.GET['delete']
    # 레코드 삭제
    delete_record = Task.objects.get(id=user_input_delete)
    delete_record.delete()
    # 다시 사이트 불러오기
    return HttpResponseRedirect(reverse('index'))

# 할일 완료 task
def complete_task(request):
    # 완료한 할일
    user_input_complete = request.POST['complete']
    # 체크 표시
    complete_record = Task.objects.get(id=user_input_complete)
    complete_record.iscompleted = not complete_record.iscompleted
    complete_record.save(update_fields=['iscompleted'])
    # 다시 사이트 불러오기
    return HttpResponseRedirect(reverse('index'))
