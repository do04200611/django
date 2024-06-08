django\mysite> python manage.py shell
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information       
IPython 8.7.0 -- An enhanced Interactive Python. Type '?' for help. 

In [1]: from polls.models import Cho
   ...: ice, Question

In [2]: from polls.models import Choice, Question

In [3]: Question.objects.all()
Out[3]: <QuerySet [<Question: What's up?>, <Question: questions>, <Question: 이순신>, <Question: java>]>

In [4]: from django.utils import timezone

In [5]: q = Question(question_text="What's Subject?", pub_date=time 
   ...: zone.now())

In [6]: q.save()

In [7]: q.id
Out[7]: 5

In [8]: q.question_text
Out[8]: "What's Subject?"

In [9]: q.pub_date
Out[9]: datetime.datetime(2024, 6, 8, 7, 39, 18, 169620, tzinfo=datetime.timezone.utc)

In [10]: q.question_text = "무슨 과목 좋아해?"

In [11]: q.question_text = "What's Subject?"

In [12]: q.save()

In [13]: Question.objects.all()
Out[13]: <QuerySet [<Question: What's up?>, <Question: questions>, <Question: 이순신>, <Question: java>, <Question: What's Subject?>]>  

In [14]: from polls.models import Choice, Question

In [15]: Question.objects.all()
Out[15]: <QuerySet [<Question: What's up?>, <Question: questions>, <Question: 이순신>, <Question: java>, <Question: What's Subject?>]>  

In [16]: Question.objects.filter(id=1)
Out[16]: <QuerySet [<Question: What's up?>]>

In [17]: Question.objects.filter(question_text__startswith="What")  
Out[17]: <QuerySet [<Question: What's up?>, <Question: What's Subject?>]>

In [18]: from django.utils import timezone

In [19]: current_year = timezone.now().year

In [20]: Question.objects.get(pub_date__year=current_year)
--------------------------------------------------------------------
MultipleObjectsReturned            Traceback (most recent call last)
Cell In[20], line 1
----> 1 Question.objects.get(pub_date__year=current_year)

File ~\AppData\Local\Programs\Python\Python310\lib\site-packages\django\db\models\manager.py:87, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs) 
     85 @wraps(method)
     86 def manager_method(self, *args, **kwargs):
---> 87     return getattr(self.get_queryset(), name)(*args, **kwargs)

File ~\AppData\Local\Programs\Python\Python310\lib\site-packages\django\db\models\query.py:652, in QuerySet.get(self, *args, **kwargs)  
    648 if not num:
    649     raise self.model.DoesNotExist(
    650         "%s matching query does not exist." % self.model._meta.object_name
    651     )
--> 652 raise self.model.MultipleObjectsReturned(
    653     "get() returned more than one %s -- it returned %s!"    
    654     % (
    655         self.model._meta.object_name,
    656         num if not limit or num < limit else "more than %s" % (limit - 1),
    657     )
    658 )

MultipleObjectsReturned: get() returned more than one Question -- it returned 5!

In [21]: Question.objects.get(pk=1)
Out[21]: <Question: What's up?>

In [22]: q = Question.objects.get(pk=1)

In [23]: q.was_published_recently()
Out[23]: True

In [24]: q = Question.objects.get(pk=1)

In [25]: q.choice_set.all()
Out[25]: <QuerySet [<Choice: Not much>, <Choice: The sky>]>

In [26]: q.choice_set.create(choice_text="파이썬", votes=0)
Out[26]: <Choice: 파이썬>

In [27]: q.choice_set.create(choice_text="자바", votes=0)
Out[27]: <Choice: 자바>

In [28]: c = q.choice_set.create(choice_text="C언어", votes=0)      

In [29]: c.question
Out[29]: <Question: What's up?>

In [30]: q.choice_set.all()
Out[30]: <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: 파이썬>, <Choice: 자바>, <Choice: C언어>]>

In [31]: q.choice_set.count()
Out[31]: 5

In [32]: Choice.objects.filter(question__pub_date__year=current_yea 
    ...: r)
Out[32]: <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: 파이썬>, <Choice: 자바>, <Choice: C언어>]>

In [33]: c = q.choice_set.filter(choice_text__startswith="자바")    

In [34]: c.delete()
Out[34]: (1, {'polls.Choice': 1})

In [35]:
