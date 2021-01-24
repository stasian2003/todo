from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import BShop

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()

    return render(request, 'test.html', {"todo_list":todo_list})

def books(request):
    book_list = BShop.objects.all()

    return render(request, 'books.html', {"book_list":book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    bshop = BShop(title=title)
    bshop.save()
    return redirect(books)

