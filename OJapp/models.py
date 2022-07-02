from django.db import models
from django.contrib.postgres.fields import ArrayField
from ckeditor.fields import RichTextField
from django.forms import CharField
class question(models.Model):
    questionTitle=models.CharField(max_length=100)
    # question=models.CharField(max_length=255)
    question=RichTextField(blank=True,null=True)
    def __str__(self):
        return self.questionTitle
class testCase(models.Model):
    questionTitle = models.ForeignKey(question, on_delete=models.CASCADE)
    # Input=RichTextField(blank=True,null=True)
    array=[('a','r')] 
    test=models.CharField(choices=array,max_length = 200,null=True)
    Input=models.TextField(max_length = 200,null=True) 
    ExpectedOutput=models.TextField(max_length = 200)
    def __str__(self):
        return str(self.questionTitle) 