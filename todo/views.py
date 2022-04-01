from django.shortcuts import render
from .models import todoDataSet

# Create your views here.

def index(request):
    context = {'data': todoDataSet.objects.all()}
    if request.method == "POST" and 'addData' in request.POST:
        print("queryDict IS: ",request.POST)
        print("python Dict IS: ",dict(request.POST))
        print("values is: ",dict(request.POST)['nameText'])
        if bool(request.POST['myID']):
            todoDataSet.objects.filter(id=request.POST['myID']).update(name=request.POST['nameText'],age=request.POST['age'],address=request.POST['description'])
        else:
            todoDataSet(name=request.POST['nameText'],age=request.POST['age'],address=request.POST['description']).save()
    if request.method == "POST" and 'deleteData' in request.POST:
        todoDataSet.objects.get(id=request.POST['deleteData']).delete()
    if request.method == "POST" and 'updateData' in request.POST:
        upData = todoDataSet.objects.get(id=request.POST['updateData'])
        print("SDSDSD",upData.name)
        context['formData'] = [upData.id,upData.name,upData.age,upData.address]
    return render(request,'todo/index.html',context)

# def 
