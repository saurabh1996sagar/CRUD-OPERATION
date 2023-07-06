from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def index(request):
    emp = Employee.objects.all()
    return render(request, 'index.html', {'employee': emp})

def add(request):
    if request.method == 'POST':
        username = request.POST['name']
        userdeptt = request.POST['deptt']
        useraddress = request.POST['address']

        employee = Employee(name=username, address=useraddress, deptt_id=userdeptt)
        employee.save()

        return redirect("/")

    else:    
       return render(request, 'add-new.html')

def posts(request):
    posts = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'posts.html', {'p': posts})

def post(request, pk):
    return render(request, 'post.html', {'value': pk})
  

def update(request, pk):
    employee = Employee.objects.get(id=pk)
    return render(request, 'update.html', { 'emp': employee })

def changedata(request, pk):
    username = request.POST['name']
    userdeptt = request.POST['deptt']
    useraddress = request.POST['address']
   
    emp = Employee.objects.get(id=pk)
    emp.name = username
    emp.deptt_id = userdeptt
    emp.address = useraddress
    emp.save()

    return redirect("/")

def delete(request, pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return redirect("/")

