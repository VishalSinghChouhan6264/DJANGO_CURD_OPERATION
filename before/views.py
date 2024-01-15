from django.shortcuts import render,redirect
from django.http import HttpResponse

from before.forms import EmployeeForm
# Create your views here.
from .models import Post,Employee

def backend(request):
    return HttpResponse("We learn django app")

def create(request):
    if request.method=="POST":
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title=request.POST.get('title')
            post.content=request.POST.get('content')
            post.save()
            return render(request,'first.html')
    else:
        return render(request,'first.html')
    

# curd function

def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            
            except:
                pass
    else:
        form=EmployeeForm
    return render(request,'index.html',{'form':form})


def show(request):
    employees=Employee.objects.all()
    context = {'employee':employees}
    
    return render(request,'show.html',context)

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employee})

def desk(request):
    return HttpResponse("hello everyone")

