from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader



#key value : JsonResponse
#key or value:HttpResponse

def index(request):
    return render(request,"Home/index.html")


def about(request):
        return render(request,"about/index.html")

def services(request):
    return render(request,"services/index.html")
def form(request):
    return render(request,"Form/form.html")
def submitMyform(request):
    my_dict={
        "Name":request.POST['name'],
        "Address":request.POST['add'],
        "Password":request.POST['pass'],
        "Method":request.method

    }
    return  JsonResponse(my_dict)

def contact(request):
    var="Hello",
    greeting="How are you",
    list=["hh", 4, "eefs"],
    num1,num2=36,69,
    ans=num1>num2

    my_dict={
         "aa":var,
         'msg':greeting,
         'li':list,
         "num1":num1,
         "num2":num2,
         "ans":ans
    }
    return render(request,"contact/index.html", context=my_dict)

def images(request):
    return render(request,"images/images.html")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    my_dict={
        "Name":name,
        "Age":age
    }
    return JsonResponse(my_dict)
    