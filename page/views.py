from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models  import User_data
from django.contrib import messages
from .models import Anthologies
# Create your views here.
def index(request):
    anthologies=Anthologies.objects.all()
    return render(request,'index.html',{'anthologies':anthologies})

def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User_data.objects.filter(name=name,email=email,password=password).exists():
            messages.info(request,'Welcome {}'.format(name))
            return redirect(index,permanent=True)
        messages.info(request,"Not a valid user")
        return redirect(login,permanent=True)
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        date=request.POST.get('date')
        if password1!= password2:
            messages.info(request,'Please type the same password')
            return redirect(signup,permanent=True)
        deatil=User_data(name=name,email=email,number=number,address=address,city=city,state=state,password=password1,date=date)
        deatil.save()
        return redirect(index,permanent=True)
    return render(request,'signup.html')