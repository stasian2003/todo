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
    subtitle = form["book_subtitle"]
    discription = form["book_discription"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    bshop = BShop(year=year, title=title, author=author, price=price, subtitle=subtitle, discription=discription, genre=genre)
    bshop.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def todo(request, id):
    todo_object = ToDo.objects.filter(id=id)
    return render(request, 'todo.html', {"todo_list":todo_object})