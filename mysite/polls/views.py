from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # 템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려줌
    # Django 에서 제공하는 Shortcuts 표현 ↑
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # 404 에러 일으키기
    # get_object_or_404()함수는 Django 모델을 첫번째 인자로 받고
    # 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
    # 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
