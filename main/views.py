from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import BookStore

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()

    return render(request, 'test.html', {"todo_list":todo_list})

def third(request):
     book_store = BookStore.objects.all()

    return render(request, 'test.html', {"book_store":book_store})