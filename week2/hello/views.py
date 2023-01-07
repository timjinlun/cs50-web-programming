from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 该界面是针对目前已创建的"hello"app，下方列举的functions是该app的function。
def index(request):
    return render(request, "hello/index.html")

def tim(request):
    return HttpResponse("Hello, Tim!")


# 基于自定义路径的function：为避免重复创建冗余的url路径。以下是案例function：
"""def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")"""

# 该function加入了动态,具体说明查看CS50WebProgram lecture2, 34:08;"name" is a variable
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })
