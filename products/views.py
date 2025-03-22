from django.shortcuts import render
from .models import Category ,Product
# Create your views here.

def home(request):
    context = {}
    return render(request,'products/home.html',context)

def menu(request):
    product_opj = Product.objects.all()
    category_opj = Category.objects.all()
    context = {
        'product':product_opj,
        'category':category_opj,       
        }
    return render(request,'products/menu.html',context)
    
def about(request):
    context = {}
    return render(request,'products/about.html',context)
    
def contact(request):
    context = {}
    return render(request,'products/contact.html',context)
