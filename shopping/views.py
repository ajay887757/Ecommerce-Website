from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from shopping.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint

def All_category():
    allcat=category.objects.all()
    return allcat

def Home(request):
    d={"allcat":All_category()}
    print(d)
    return render(request,'index.html',d)
def About(request):
    d = {"allcat": All_category()}
    return render(request,'about.html',d)
def contact(request):
    d = {"allcat": All_category()}
    return render(request,'contact.html',d)
def blog(request):
    d = {"allcat": All_category()}
    return render(request, 'blog.html',d)
def cart(request):
    d = {"allcat": All_category()}
    return render(request, 'cart.html',d)
def shop(request,cid):
    catdata=category.objects.get(id= cid)
    subdata=sub_category.objects.filter(category=catdata).first()
    #pro=products.objects.filter(sub_category=subdata)
    d = {"allcat": All_category(),"catdata":catdata,"subdata":subdata}
    return render(request, 'shop.html',d)