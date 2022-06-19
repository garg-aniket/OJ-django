from django.db import models


class question(models.Model):
    questionTitle=models.CharField(max_length=100)
    question=models.CharField(max_length=255)
    
    def __str__(self):
        return self.questionTitle