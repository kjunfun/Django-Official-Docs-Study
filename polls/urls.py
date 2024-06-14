from django.urls import path
# 현재 디렉토리(.)에서 views 모듈을 가져옴. 
from . import views

# views.py에는 URL패턴에 따라 호출될 함수들이 정의되어 있어야 함.
app_name = "polls"
urlpatterns = [
    # ex) /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex) /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex) /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex) /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]