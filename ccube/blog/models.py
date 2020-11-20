from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now
from django_currentuser.middleware import get_current_user
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + 'by' + self.author

    def enroll(self, user):
        try:
            registered = AssignCourses.objects.get(user=user, post=self)
            if registered:
                return False
        except:
            registration = AssignCourses.objects.create(user=user, post=self)
            return True

    def deroll(self, user):
        try:
            registered = AssignCourses.objects.get(user=user, post=self)
            if registered:
                registered.delete()
                return True
        except:
            return False

    def check_enroll(self):
        try:
            registered = AssignCourses.objects.get(
                user=get_current_user(), post=self)
            if registered:
                return True
        except:
            return False


class SideBar(models.Model):
    first_mark = models.CharField(max_length=100)
    Second_mark = models.CharField(max_length=100)
    Third_mark = models.CharField(max_length=100)
    fourth_mark = models.CharField(max_length=100)
    fifth_mark = models.CharField(max_length=100)
    course = models.ManyToManyField("Post")

# class Quizetaker(models.Model):


class Quiz(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    question = models.TextField(max_length=355)
    course = models.ManyToManyField("Post")


class Response(models.Model):
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    rightans = models.CharField(max_length=100, default="")
    # is_correct = models.BooleanField(default=False)
    quiz = models.ManyToManyField("Question")

# class AnswerCheck(models.Model):


class quiztaker(models.Model):
    # user = models.ForeignKey("User",  on_delete=models.CASCADE)

    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class userans(models.Model):
    quiz_taker = models.ForeignKey("quiztaker",  on_delete=models.CASCADE)
    answer = models.ForeignKey("Response", on_delete=models.CASCADE)


class AssignCourses(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
