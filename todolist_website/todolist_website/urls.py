"""
URL configuration for todolist_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #HTTP 프로토콜 요청이 들어오면 todolist.urls 모듈에 정의된 URL 패턴으로 전달
    path("",include("todolist.urls")),
    #장고 관리자 사이트를 위한 URL 패턴
    path('admin/', admin.site.urls),
]


# setting.py에 있는 static 파일 연결
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
