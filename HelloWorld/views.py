from django.http import HttpResponse
from django.urls import reverse

def hello(request):
    s = "Hello World!<br/导航列表:<br/>" + \
        "<a href='"+reverse("about")+"'>关于HelloWorld</a><br/>" + \
        "<a href='"+reverse("weather")+"'>关于天气</a>"
    return HttpResponse(s)