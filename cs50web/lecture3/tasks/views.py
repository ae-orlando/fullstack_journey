from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") # field

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)        #save submited value to the form
        if form.is_valid():                     # xheck if form is valid.
            task = form.cleaned_data["task"]    #get the data on the form and put it in a variable called task
            request.session["tasks"] += [task]                     # add the data to the list 
            return HttpResponseRedirect(reverse("index"))

        else:                                   # if the form is invalid, they see the form they submitted so they can see their errors.
            return render(request, "tasks/add.html", {
                "fr": form
            })
    
    return render(request, "tasks/add.html", {
        "fr": NewTaskForm()                     #giving the template access to the form
    })