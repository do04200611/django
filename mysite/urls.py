
from django.contrib import admin
# URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달합니다.

from django.urls import include, path

urlpatterns = [
    #polls 사이트 지정
    path("polls/", include("polls.urls")),

    # admin 사이트 지정
    path("admin/", admin.site.urls),
]