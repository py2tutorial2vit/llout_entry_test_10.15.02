from django.db import models

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self): return self.chapter_name

class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    responsed=models.BooleanField(default=False)
    quote_text = models.CharField(max_length=255, blank=True, default='')
    #question_text = models.CharField(max_length=255)
    question_text = models.TextField(max_length=420, default='')
    
    
    def __str__(self): return self.question_text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,default='')
    #chapter = question.chapter
    response_text = models.TextField(max_length=1255,default='')
    
    def __str__(self): return self.response_text[:20]
