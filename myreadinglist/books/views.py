from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

# from .forms import BookForm
from .models import Book, BookForm


def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/index.html", context)


def book_info(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(pk = book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/books")

    try:
        book = Book.objects.get(pk=book_id)
        form = BookForm(instance=book)
        context = {"book": book, "form": form}
    except Book.DoesnotExist:
        raise Http404("Requested book does not exist")
    return render(request, "books/info.html", context)


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/books")
        else:
            print(form.is_valid())
            print(form.errors)
    else:
        form = BookForm()
    return render(request, "books/new.html", {"form": form})
