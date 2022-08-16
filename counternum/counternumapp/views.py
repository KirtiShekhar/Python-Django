from django.shortcuts import render,redirect
from .models import CounterNumberModel

# Create your views here.
def hellostudent(request):
    SchoolName = "Bal Bharati Public School"
    schoolContext = {'SchoolName': SchoolName}
    return render(request,"hellostudent/hellostudent.html",schoolContext)

def counternum(request):
    numberObject = CounterNumberModel.objects.filter(id = 1)[0]
    counterNumber = numberObject.number
    numberContext = {'counterNumber': counterNumber}
    return render(request,"counternum/counternum.html",numberContext)

def increment(request):
    # code to increment the number
    numberObject = CounterNumberModel.objects.filter(id = 1)[0]
    numberObject.number = int(numberObject.number)+1
    numberObject.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    # code to decrement the number
    numberObject = CounterNumberModel.objects.filter(id=1)[0]
    numberObject.number = int(numberObject.number) - 1
    numberObject.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    # code to reset the number to 0
    numberObject = CounterNumberModel.objects.filter(id=1)[0]
    numberObject.number = 0
    numberObject.save()
    return redirect(request.META['HTTP_REFERER'])