from django.urls import path

from . import views

# URL指的是网页的路径，而urlpatterns则是对网页路径的设定，这样一来，当用户输入特定关键词后，
# 便能够进入该路径，从而获取该路径下的网页信息。

# 该urlpattern是针对某一特定app所设定的url触发机制，当关键词被触发之后，即运行该app中指定的function。

# path后设定的第一个argument意义在于，当用户在根目录"\"之后添加该argument，该argument将传回服务端的views.py，
# 找到并触发与该argument对应的function，最终上传并响应到用户的网页端上。

urlpatterns = [
    
# 生成自定义路径：用户输入的type为string的variable，都将触发views.greet function，且该variable将作为function的parameter用以触发
    path("<str:name>", views.greet, name="greet"),
    path("", views.index, name="index"),
    path("tim", views.tim, name="tim") 
]

