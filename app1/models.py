from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

class Answer(models.Model):
    answer_options=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=100)