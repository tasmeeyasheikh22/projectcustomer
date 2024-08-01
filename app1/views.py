from django.shortcuts import render,redirect
from .forms import CustomerForm
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def addview(request):
    form = CustomerForm()
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})

def showview(request):
    obj = Customer.objects.all()
    return render(request,"app1/show.html",{"cust":obj})




def updateview(request,ud):
    obj = Customer.objects.get(cid=ud)
    form = CustomerForm(instance=obj)
    if request.method == "POST":
        form = CustomerForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})

def deleteview(request,id):
    obj = Customer.objects.get(cid=id)
    obj.delete()
    return redirect("/a1/sv/")