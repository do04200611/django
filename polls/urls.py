from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

#  app_name을 추가하여 어플리케이션의 이름공간을 설정할 수 있습니다.
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]