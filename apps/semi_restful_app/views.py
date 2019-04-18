from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.

def  new (request):
     return render ( request, 'index.html')


def create (request):
     errors = Show.objects.validate(request.POST)
     if errors:
        for error in errors:
             messages.error(request, error)
        return render(request,'index.html')
     else:
        show_id = Show.objects.easy_show_create (request.POST)
        return redirect('/shows/' + str(show_id))
   
   

def view(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

    
def edit (request, show_id):
    context = { 
         "show" : Show.objects.get(id=show_id),
    }
    return render (request, 'edit.html', context)

def update(request, show_id):
    show = Show.objects.easy_show_update (request.POST, show_id)
    return redirect ('/shows/new/')

def display(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    return render(request, 'views.html', context)