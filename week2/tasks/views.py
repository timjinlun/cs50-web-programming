from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    # 这是一个key:value pair, 右边的是value，左边的是key;value是line 4 list 内的值；key是当使用django渲染index.html时，html将要获取的variable名称
    # 具体查看CS50 Week3 56:35
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]    
    })

def add(request): # 1:27:15
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form":form
            })
    return render(request, "tasks/add.html",{  # give this template access to a variable called form, which will be NewTaskForm
        "form": NewTaskForm()
    })