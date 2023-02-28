from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Apple
from .forms import AppleForm



# Create your views here.
def index(request):
    apple=Apple.objects.all()
    context={
        'apple_site':apple

    }
    return render(request,"index.html",context)

def nextpage(request,apple_id):
    apple=Apple.objects.get(id=apple_id)
    return render(request,'nextpage.html',{'apple':apple})

def add_apple(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        apple=Apple(name=name,desc=desc,year=year,img=img)
        apple.save()
    return render(request,'add.html')

def update(request,id):
    apple=Apple.objects.get(id=id)
    form=AppleForm(request.POST or None, request.FILES,instance=apple)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'apple':apple})
def delete(request,id):
    if request.method=='POST':
        apple=Apple.objects.get(id=id)
        apple.delete()
        return redirect('/')
    return render(request,'delete.html')
