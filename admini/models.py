from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Question(models.Model):
    identification = models.IntegerField()
    questionText = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
    CHOICES = (
        ('1', answer1),
        ('2', answer2),
        ('3', answer3),
        ('4', answer4),
    )
    rightAnswer = models.CharField(max_length=20, choices=CHOICES)
    difficulty = models.IntegerField()
    topic = models.CharField(max_length=20)     # theme de la question
    score = models.IntegerField()   # points rapportes

    def __str__(self):
        return self.questionText


class Stats(models.Model):
    nbrQ=models.IntegerField()
    nbrJ=models.IntegerField()
    nbrJConnected=models.IntegerField()


