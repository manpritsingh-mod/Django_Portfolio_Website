from django.http import request
from django.shortcuts import render
from pro.models import aut,new,deleteitem



# Create your views here.
def login(request):
    return render(request,"login.html")

def regi(request):
    return render(request,"regi.html")

def fp(request):
    return render(request,"fp.html")

def dele(request):
    return render(request,"delete.html")

def search(request):
    return render(request,"search.html")

def add(request):
    return render(request,"add.html")

def show(request):
    return render(request,"show.html")

def logo(request):
    return render(request,"login.html")

def adding(request):
    if request.method=="POST":
        n=request.POST["name"]
        ph=request.POST["phone"]
        un=request.POST["username"]
        pa=request.POST["pass"]
        re=n=request.POST["repass"]
        if  pa==re:
            d=aut(name=n,user=un,phone=ph,passw=pa)
            d.save()
            return render(request,"login.html")
        else:
            return render(request,"regi.html")


def logg(request):
    if request.method=="POST":
        u=request.POST['user']
        p=request.POST['pass']
        de=aut.objects.get(user=u,passw=p)
        return render(request,"add.html")
         
    return render(request,"login.html")


def delet(request):
    d=new.objects.all()
    return render(request,"delete.html",{'sc':d})

def newdata(request):
    if request.method=="POST":
        a=request.POST["adh"]
        n=request.POST["name"]
        q=request.POST["quali"]
        ad=request.POST["add"]
        ad1=request.POST["add1"]
        c=request.POST["city"]
        st=request.POST["state"]
        zi=request.POST["zip"]
        s=new(adh=a,name= n,qua=q,add1=ad,add2=ad1,city=c,state=st,zip=zi)
        s.save()
        return render(request,"add.html")

def serh(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
    d=new.objects.get(adh=adhar)
    return render(request,'search.html',{'sc':d})

def dele(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
         d=new.objects.filter(adh=adhar)
         d.delete()
         d=new.objects.all()
         return render(request,"delete.html",{'sc':d})

def adserch(request):
    if request.method=="POST":
         ph=request.POST["aad"]
         d=aut.objects.get(phone=ph)
         return render(request,'fp.html',{'sc':d})

def paswd(request):
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

def deltem(request):
    if request.method=="POST":
         adhar=request.POST["aad"]
    d=new.objects.get(adh=adhar)
    return render(request,'delit.html',{'sc':d})





