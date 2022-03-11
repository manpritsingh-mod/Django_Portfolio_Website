
from django.contrib import auth
from django.shortcuts import redirect, render
from record.models import aut,deta,deleteitem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def logi(request):
    return render(request,"login.html")

def deleti(request):
    d=deta.objects.all()
    return render(request,"delete.html",{'sc':d})
    

def regi(request):
         return render(request,"regi.html")

def ser(request):
        
         return render(request,"search.html")

def show(request):
         d=deta.objects.all()
         return render(request,"show.html",{'sc':d})

def regsave(request):
    
    if request.method=="POST":
        n=request.POST["name"]
        p=request.POST["phone"]
        un=request.POST["username"]
        pa=request.POST["pass"]
        rpa=request.POST["repass"]
        if pa==rpa:   
            d=aut(nm=n,pho=p,username=un,password=pa)
            d.save()           
            return render(request,"login.html")
        else:
            
            return render(request,"regi.html")

def log(request):
    if request.method=="POST":
        try:
            u=request.POST["user"]
            p=request.POST["pass"]
            de=aut.objects.get(username=u,password=p)
            request.session["username"]=de.username
            return render(request,"add.html")
        except:
            return render(request,"login.html")

def add(request):
     return render(request,"add.html")

def adddata(request):
    if request.method=="POST":
        a=request.POST["adh"]
        n=request.POST["name"]
        q=request.POST["quali"]
        ad=request.POST["add"]
        ad1=request.POST["add1"]
        c=request.POST["city"]
        st=request.POST["state"]
        zi=request.POST["zip"]
        s=deta(adh=a,name= n,qua=q,add1=ad,add2=ad1,city=c,state=st,zip=zi)
        s.save()
        return render(request,"add.html")


def serch(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
    d=deta.objects.get(adh=adhar)
    return render(request,'search.html',{'sc':d})


def dele(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
         d=deta.objects.filter(adh=adhar)
         d.delete()
         d=deta.objects.all()
         return render(request,"delete.html",{'sc':d})
         

def logo(request):
    logout(request)
    return render(request,"login.html")

def fp(request):
    return render(request,'fp.html')


def adserch(request):
    if request.method=="POST":
         ph=request.POST["aad"]
    d=aut.objects.get(pho=ph)
    return render(request,'fp.html',{'sc':d})

def pwu(request):
   if request.method=="POST":
        n=request.POST["name"]
        p=request.POST["phone"]
        un=request.POST["username"]
        pa=request.POST["pass"]
        rpa=request.POST["repass"]
        s=aut.objects.filter(pho=p)
        s.delete()
        if pa==rpa:   
                d=aut(nm=n,pho=p,username=un,password=pa)
                d.save()           
                return render(request,"login.html")
        else:
            
            return render(request,"regi.html")

def ditem(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
    d=deta.objects.get(adh=adhar)
    return render(request,'delit.html',{'sc':d})

def up(request):
    return render(request,"delit.html")