from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post,  AssignCourses, Quiz, Question, Response, quiztaker, userans
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def allblogs(request):
    allPosts = Post.objects.all()

    context = {'allPosts': allPosts}
    if request.method == "POST":
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_Dk1stp553UnTd6','MacUrC3nKYIZyosEVci4IsGG'))
        payment = client.order.create({'amount':amount, 'currency': 'INR', 'payment_capture':'1'})
    return render(request, "blog/allblogs.html", context)

@csrf_exempt
def success(request):
    return render(request, 'blog/success.html')

def blogHome(request):
    allPosts = AssignCourses.objects.filter(user=request.user)

    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()

    context = {'post': post}
    return render(request, "blog/blogPost.html", context)


@login_required
def enroll(request, slug):
    this_event = Post.objects.get(slug=slug)
    this_event.enroll(user=request.user)

    messages.success(request, "You have successfully enrolled the course.")
    return redirect("bloghome")


@login_required
def deroll(request, slug):
    this_event = Post.objects.get(slug=slug)
    this_event.deroll(user=request.user)
    messages.error(request, "You have successfully unenrolled the course.")
    return redirect("bloghome")


def check_enroll(request, slug):
    try:
        this_event = Post.objects.get(slug=slug)
        registered = AssignCourses.objects.get(
            user=request.user, post=this_event)
        if registered:
            return True
    except:
        return False


def simulations(request):

    return render(request, "blog/simulations.html")


def quiz(request):
    ques = Question.objects.all()
    resp = Response.objects.all()
    return render(request, "blog/quiz.html", {'questions': ques, 'response': resp})


def video(request):
    return render(request, "blog/video.html")


def questions(request):
    ques = Question.objects.all()
    context = {'questions': ques}
    return render(request, "blog/quiz.html", context)


def response(request):
    resp = Response.objects.all()
    context = {'response': resp}
    return render(request, "blog/quiz.html", context)
