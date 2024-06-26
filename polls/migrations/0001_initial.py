# 이 파일은  저장된 새 모델에 대한 migration을 읽어볼 수 있습니다. 

# Generated by Django 5.0.6 on 2024-06-07 14:21

import django.db.models.deletion
from django.db import migrations, models

# Migration은 Django가 모델(즉, 당신의 데이터베이스 스키마)의 변경사항을 디스크에 저장하는 방법입니다. 

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
