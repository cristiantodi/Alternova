from django.shortcuts import render
from posts.models import Post
from categories.models import Category
from tipo.models import Tipo

# Create your views here.

def home(request):
    post=Post(request)
    detalle=Post.objects.all()
    return render(request,"index.html", {"detalle": detalle})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    detalle=Post.objects.filter(category=category)
    return render(request, "category.html", {'category':category}, {"detalle": detalle})

def tipo(request, tipo_id):
    tipo = Tipo.objects.get(id=tipo_id)
    detalle=Post.objects.filter(tipo=tipo)
    return render(request, "tipo.html", {'tipo':tipo}, {"detalle": detalle})