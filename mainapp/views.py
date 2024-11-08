from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    hom=homePage.objects.all()
    return render(request,"mainapp/index.html",context={"hom":hom})


def showservice(request,adad):
    ser=serviceClass.objects.filter(category_id=adad)

    return render(request,"mainapp/showServices.html",context={"ser":ser})


def about(request):
    st=staticContentClass.objects.get(key='about')
    return render(request,"mainapp/about.html",context={"matn":st})

def services(request):
    cat=categoryClass.objects.all()
    return render(request,"mainapp/services.html",context={"cat":cat})

def t(request):
    return render(request,"mainapp/t.html")

def contact(request):
    if (request.method=="POST"):
        f=contactForm(request.POST)
        if (f.is_valid):
            f.save()
            return redirect("/contact")
    else:        
        f=contactForm()
        st=staticContentClass.objects.get(key='contact')
        return render(request,"mainapp/contact.html",context={"f":f,"matn":st})