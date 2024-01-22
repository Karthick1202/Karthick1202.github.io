from django.shortcuts import render
from django.http import HttpResponse
from .forms import mobileform,amazonform
from .models import mobile,amazon
# Create your views here.

def addmobileview(request):
    form=mobileform()
    if request.method=="POST" and request._files:
        form=mobileform(request.POST,request._files)
        if form.is_valid():
            form.save()
            return HttpResponse('Mobile Phone Added Sucessfully')
    return render(request,'mobile.html',{'form':form})


def displayview(request,id):
    data=mobile.objects.get(id=id)
    return render(request,'display.html',{'data':data})


def amazonview(request):
    form=amazonform()
    if request.method=="POST" and request._files:
        form=amazonform(request.POST,request._files)
        if form.is_valid():
            form.save()
            return HttpResponse('Mobile Phone Added Sucessfully')
    return render(request,'addmobile.html',{'form':form})


def displayallview(request):
    data=amazon.objects.all()
    return render(request,'displayall.html',{'data':data})

def displayamazonview(request,id):
    data=amazon.objects.get(id=id)
    return render(request,'displayone.html',{'data':data})

# def delete(request,pk):
#     return render(request,'del.html',{'pk':amazon.objects.get(id=pk).delete()})