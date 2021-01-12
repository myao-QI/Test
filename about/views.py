from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def about(request):
    s = "哈啰啊！<br/>姓名：XXX<br/>学号：XXX<br/>" + \
        "<a href = '"+reverse("hello")+"'>返回首页</a>"
    return HttpResponse(s)