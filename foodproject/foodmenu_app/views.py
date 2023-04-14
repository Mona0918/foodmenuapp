from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ItemModel
from .forms import AddItemForm
from django.urls import reverse

def index(request):
    item_list = ItemModel.objects.all()
    return render(request,"index.html",{"items":item_list})

def itemview(request):
    return HttpResponse("<h1>This is an Item View</h1>")

def detailview(request,item_id):
    data=ItemModel.objects.get(pk=item_id)
    return render(request,"detailitem.html",{"context":data})

def additemview(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form= AddItemForm()
        return render(request,'additem.html',{'form':form})

def updateitemview(request,pk):
    item=ItemModel.objects.get(id=pk)
    form=AddItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))
    return render(request,'additem.html',{'form':form,'item':item})

def deleteitemview(request,pk):
    item = ItemModel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(reverse('index'))
    return render(request,'deleteitem.html',{'item':item})


