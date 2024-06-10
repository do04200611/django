# 클라이언트로부터 받은 URL 요청을 어떻게 처리할것인지 정의하는 파

# =============================

# route 와 view, 2개의 선택 가능한 인수로 kwargs 와 name 까지 모두 4개의 인수가 전달 되었습니다. 
from django.urls import path

from . import views

#  app_name을 추가하여 어플리케이션의 이름공간을 설정할 수 있습니다.
app_name = "polls"
urlpatterns = [
    #설문조사 어플리케이션을 위해 아래에 나와있는 코드를 포함하는 URLconf
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

]