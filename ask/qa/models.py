from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.CharField(max_length=255)
    def __unicode__(self):
        return self.title
    #def get_absolute_url(self):
    #    return '/post/%d/' % self.pk
    #class Meta:
    #    db_table = 'blogposts'
    #    ordering = ['-creation_date']
class Answer(models.Model):
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ManyToManyField(Question)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.title

# Create your models here.
