from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import List


# Create your views here.
def home(request):
    msg = ""
    if request.method == "POST":
        heading = request.POST['heading']
        desc = request.POST['description']
        status = request.POST['status']

        params = List.objects.create(heading=heading,description=desc,status=status)
        msg = "Data saved successfully"
    # return HttpResponse('this is home page')
    return render(request,'index.html',{'msg':msg})
 

def show_data(request):
    data = List.objects.all()

    show = {
        'data':data
    }

    return render(request,'show_data.html',show)

def update(request,id):
    var = List.objects.get(id=id)

    return render(request,"update.html",{"var":var})

def updating(request,id):
    edit = List.objects.get(id=id)
    edit.heading = request.POST['heading']
    edit.description = request.POST['description']
    edit.status = request.POST['status']

    edit.save()
    return redirect('show')


def delete(request,id):
    
    var= List.objects.get(id=id)
    var.delete()
    
        
    return redirect('show')

    