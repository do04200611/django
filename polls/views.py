# 데이터와 비즈니스 로직 사이의 상호 동작을 관리하는 파
#  request 는 HttpRequest 개체
# =============================

from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

# Create your views here.

#뷰를 업데이트 하는 기능

# index() 뷰 하나를 호출했을 때, 시스템에 저장된 최소한 5 개의 투표 질문이 콤마로 분리되어, 발행일에 따라 출력됩니다.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:4]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
   
    #연결할 페이지 지정
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
     #연결할 페이지 지정
    return render(request, "polls/results.html", {"question": question})


# request.POST 는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체이며, 값은 항상 문자열들입니다. 
# HttpResponseRedirect 는 하나의 인수를 받습니다: 그 인수는 사용자가 재전송될 URL 입니다.

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #선택된 설문의 ID를 문자열로 반환
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # KeyError 를 체크하고, choice가 주어지지 않은 경우에는 에러 메시지와 함께 설문조사 폼을 다시보여줍니다.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,

                # 선택 된게 아무것도 없을 때 출력 할 메시지
                "error_message": "아무것도 선택 되지 않았습니다. 다시 선택해주세요",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)
