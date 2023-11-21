from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Author, Book, Reader, BookOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BookRentedListView(ListView):
    model = Book
    template_name = 'book_index.html'


    def get(self, request, *args, **kwargs):
        get_order = BookOrder.objects.all()
        book = Book.objects.filter(pk__in = get_order.values('book'))
        return render(request, 'book_index.html', {'book_list':book})


class BookAvailableListView(ListView):
    model = Book
    template_name = 'book_available.html'


    def get_queryset(self):
        rented_books = BookOrder.objects.values('book')
        available_books = Book.objects.exclude(pk__in=rented_books)
        return available_books



class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name']
    success_url = '/author_list'


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = '/author_list'

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_update.html'
    fields = ['name']
    success_url = '/author_list'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['title', 'author']
    success_url = '/book_list'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'author']
    success_url = '/book_list'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = '/book_list'

class ReaderListView(ListView):
    model = Reader
    template_name = 'reader_list.html'
    context_object_name = 'readers'

class ReaderCreateView(CreateView):
    model = Reader
    template_name = 'reader_create.html'
    fields = ['last_name', 'first_name', 'middle_name']
    success_url = '/reader_list'

class ReaderUpdateView(UpdateView):
    model = Reader
    template_name = 'reader_update.html'
    fields = ['last_name', 'first_name', 'middle_name']
    success_url = '/reader_list'

class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = 'reader_delete.html'
    success_url = '/reader_list'




class RegisterView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')