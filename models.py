
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=50)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    
    def __str__(self):
        return f"Submission by {self.user.username}"