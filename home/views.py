from django.shortcuts import render , get_object_or_404 , redirect
from .forms import BookForm
from home.models  import *


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()
        return redirect('/books/')
    context = {
        'form':form
    }
    return render(request,"create.html",context)


def book_update(request, id=id):
    obj = get_object_or_404(Book,id=id)
    form = BookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,"create.html",context)

def book_list(request):
    queryset = Book.objects.all()
    context = {
        "list": queryset
    }
    print(list)
    return render(request,"book_list.html",context)


def book_single(request,id):
    obj = get_object_or_404(Book,id=id)
    context = {
        "title": obj.title,
        "desciption": obj.description,
        "price": obj.price
    }
    return render(request,"book_single.html",context)


def book_delete(request,id):
    obj = get_object_or_404(Book,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/books/')
    context = {
        "obj": obj,
    }
    return render(request,"book_delete.html",context)