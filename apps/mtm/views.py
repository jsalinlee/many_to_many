from django.shortcuts import render, redirect
from .models import User, Interest

# Create your views here.
def index(req):
    # User.objects.all().delete()
    # Interest.objects.all().delete()
    context = {
        "users": User.objects.all(),
    }
    return render(req, 'mtm/index.html', context)
def add_form(req):
    return render(req, 'mtm/form.html')
def add(req):
    User.objects.add_entry(req.POST)
    return redirect('/')
def show(req, id):
    context = {
        "users": User.objects.get(id = id),
        "interests": User.objects.get(id = id).interests.all
    }
    return render(req, 'mtm/show.html', context)
