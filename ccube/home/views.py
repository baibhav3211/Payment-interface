from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.


def home(request):
    # return HttpResponse("This is homepage!")
    return render(request, 'home/home.html')


def contact(request):
    # return HttpResponse("This is cntact page!")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        # fname=request.POST['fname']
        # lname=request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name= fname
        # myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')
