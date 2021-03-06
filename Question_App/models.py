from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import pytz
import datetime
# Create your models here.

def times_ago_helper(diff):
    if diff.days > 0:
        return f'{diff.days} days ago'
    if diff.seconds < 60:
        return f'{diff.seconds} seconds ago'
    if diff.seconds < 3600:
        return f'{diff.seconds // 60} minutes ago'
    return f'{diff.seconds // 3600} hours ago'

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  #user who is logged in
    title=models.CharField(max_length=200) # title of qestion
    question=models.TextField() #question
    created_time= models.DateTimeField(auto_now=True) #question creation time
    answer_count=models.IntegerField(default=0) #total reply or answer count
    qustion_upvote=models.IntegerField(default=0) #question upvote
    question_downvote=models.IntegerField(default=0) #question q

    def times_ago(self):
        diff = timezone.now() - self.created_time
        return times_ago_helper(diff)

    def __str__(self):
        return self.question


    def get_absolute_url(self):
        return reverse('home')


class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #user who logged in
    selected_question=models.ForeignKey(Question,on_delete=models.CASCADE) #selected question for which we wants to answer
    answer=models.TextField() #answer for question
    answer_created_time=models.DateTimeField(auto_now=True) #time when user answered the question
    answer_upvote=models.IntegerField(default=0) #answer upvote
    answer_downvote=models.IntegerField(default=0) #answer downvote

    def __str__(self):
        return self.answer


    def get_absolute_url(self):
        return reverse('question-detail',kwargs={'pk':self.selected_question.id})
