
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name="allblogs"),
    path('enrollments', views.blogHome, name="bloghome"),
    # path('simulations', views.simulations, name="simulations"),
    path('quiz', views.quiz, name="quiz"),
    path('video', views.video, name='video'),
    path('success', views.success, name='success'),
    path('enroll/<slug:slug>', views.enroll, name='enroll'),
    path('deroll/<slug:slug>', views.deroll, name='deroll'),
    path('check_enroll/<slug:slug>', views.check_enroll, name='check_enroll'),
    path('<str:slug>', views.blogPost, name="blogPost"),


]
