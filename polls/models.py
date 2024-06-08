# 사용할 데이터베이스를 정의하며, 이후 마이그레이션을 거치면 코드 내용대로 테이블을 생성하는 등의 동작 수행하는 파일

# =============================

import datetime
from django.db import models
from django.utils import timezone

#Question 에는 질문과 발행일을 위한 두 개의 필드를 가집니다. 

class Question(models.Model):

    # CharField 는 문자(character) 필드를 표현
    #max_length: 데이터베이스 스키마에서만 필요한것이 아닌 값을 검증할때도 쓰이는데
    question_text = models.CharField(max_length=200)

    #  DateTimeField 는 날짜와 시간(datetime) 필드를 표현
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    

# Choice 는 선택 텍스트와 투표 집계를 위한 두 개의 필드를 가집니다.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text