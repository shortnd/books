from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "books/book_detail.html"

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'price', 'cover',]

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'price', 'cover']

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

