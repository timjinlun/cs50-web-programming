from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()  # datetime模块查看CS50 Week_2 39：30
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })