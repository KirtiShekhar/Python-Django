from django.shortcuts import render,redirect
from .models import ToDoTaskModel

# Create your views here.
def todoview(request):
    myaddedtodotask = ToDoTaskModel.objects.all()
    taskContext = {'myaddedtodotask':myaddedtodotask}
    return render(request,"todo_app/homepage.html",taskContext)

def addtodotask(request):
    # write a code to add the input task to the database
    mytodotask = request.POST['task']
    ToDoTaskModel(todotask = mytodotask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetodotask(request,taskprimarykeyid):
    # write a code to delete the specific task from database
    ToDoTaskModel.objects.filter(id=taskprimarykeyid).delete()
    return redirect(request.META['HTTP_REFERER'])

def updatetodotaskview(request,taskprimarykeyid):
     # write a code to update the specific task in the database
    edittaskcontext = {'taskprimarykeyid':taskprimarykeyid}
    return render(request,"todo_app/edittodotask.html",edittaskcontext)


def updatetodotask(request,taskprimarykeyid):
    # write a code to update the specific task in the database
    userenteredcurrenttask = request.POST['task']
    edittodotask = ToDoTaskModel.objects.filter(id=taskprimarykeyid)[0]
    edittodotask.todotask = userenteredcurrenttask
    edittodotask.save()
    return redirect(request.META['HTTP_REFERER'])