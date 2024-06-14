# get_object_or_404를 사용하면 try-except 블록을 사용하지 않아도 됨.
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# 질문 “색인” 페이지 – 최근의 질문들을 표시
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

# 질문 “세부” 페이지 – 질문 내용과, 투표할 수 있는 서식을 표시
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# 질문 “결과” 페이지 – 특정 질문에 대한 결과를 표시
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# 투표 기능 – 특정 질문에 대해 특정 선택을 할 수 있는 투표 기능을 제공
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "선택을 하세요!!",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))