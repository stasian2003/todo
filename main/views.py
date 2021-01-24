from django.shortcuts import render, HttpResponse
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

