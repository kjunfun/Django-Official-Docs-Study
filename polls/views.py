# get_object_or_404를 사용하면 try-except 블록을 사용하지 않아도 됨.
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Question

# 질문 “색인” 페이지 – 최근의 질문들을 표시
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
# 질문 “세부” 페이지 – 질문 내용과, 투표할 수 있는 서식을 표시
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
# 질문 “결과” 페이지 – 특정 질문에 대한 결과를 표시
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})
# 투표 기능 – 특정 질문에 대해 특정 선택을 할 수 있는 투표 기능을 제공
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(f"You're voting on question {question_id}.")


