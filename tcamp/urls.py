from django.urls import path

# 현재 디렉토리(.)에서 views 모듈을 가져옴. 
from . import views
# views.py에는 URL패턴에 따라 호출될 함수들이 정의되어 있어야 함.
urlpatterns = [
    path("", views.index2, name="index2"),
]