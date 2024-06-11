from django.contrib import admin

from .models import Question

#관리자에게 ‘’질문’’ 대상에는 관리 인터페이스가 있다고 알려주는 것

admin.site.register(Question)