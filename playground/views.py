from django.shortcuts import render
from django.http import HttpResponse

def sya_hello(request):
    # return HttpResponse("Hello World")
    x=1
    y=2
    return render(request, 'hello.html',{'name': 'Gajendra'})