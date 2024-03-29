from pyexpat import model
from django.db import models

# Create your models here.
class Quiz(models.Model):
    quizId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    dateCreated=models.DateField(auto_now_add=True)
    mapped=models.BooleanField(default=False)

    def __str__(self):
        return self.name
   
class Question(models.Model):
    quizId= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    totalMarks=models.IntegerField()
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CorrectAnswer(models.Model):
    quizId= models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionId=models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    correctAnswer=models.CharField(max_length=100)

    def __str__(self):
        return self.correctAnswer
   