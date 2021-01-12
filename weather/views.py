from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def weather(request):
    s = "今天天气晴朗<br/>时间：2020.10.14<br/>" + \
        "<a href = '"+reverse("hello")+"'>返回首页</a>"
    return HttpResponse(s)