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


    #__str__() 메소드를 추가하는것은 객체의 표현을 대화식 프롬프트에서 편하게 보려는 이유 말고도, 
    # Django 가 자동으로 생성하는 관리 사이트 에서도 객체의 표현이 사용되기 때문
    
    def __str__(self):
        return self.question_text

    #커스텀 메소드 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    

# Choice 는 선택 텍스트와 투표 집계를 위한 두 개의 필드를 가집니다.

class Choice(models.Model):

    #on_delete :  ForeignKeyField가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정
    #CASCADE: ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    #IntegerField
    #int 인스턴스 로 표현되는 정수입니다. 
    #일반적으로 데이터베이스에 정수를 저장하는 데 사용됩니다.
    # votes에 저장 될 기본 값을 0으로 지정
    votes = models.IntegerField(default=0)
    
    #__str__() 메소드를 추가하는것은 객체의 표현을 대화식 프롬프트에서 편하게 보려는 이유 말고도, 
    # Django 가 자동으로 생성하는 관리 사이트 에서도 객체의 표현이 사용되기 때문
    
    def __str__(self):
        return self.choice_text