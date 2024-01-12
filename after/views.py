from django.shortcuts import render
from django.http import HttpResponse



def  hello(request):
    return HttpResponse("hello everyone")

def home(request):
    
    return render(request,"home.html")
def back1(request):
    data={
        "title":"Home_Page",
        "Subject":["c","c++","python","java"],
        "name":"ram",
        "phone":"94453958",
        "stud_list":[
            {"name":"pradeep","phone":95845345},
            {"name":"abhishek","phone":7654334},
        ],
        
    }
    return render(request,"home.html",data)