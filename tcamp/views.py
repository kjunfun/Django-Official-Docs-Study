from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
    return HttpResponse("장고 공식문서를 보며 훈련하기")

