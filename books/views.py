from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Book, Review

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin ,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'

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

class SearchResultsView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['review',]
    template_name = 'books/review_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = Book.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        book = Book.objects.get(pk=self.kwargs['pk'])
        obj.author = self.request.user
        obj.book = book
        obj.save()
        return HttpResponseRedirect(reverse_lazy('book_detail', args=[book.pk]))

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['review',]
    template_name = 'books/review_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = Book.objects.get(pk=self.kwargs["book_pk"])
        return context

    def form_valid(self, form):
        form.save()
        book = Book.objects.get(pk=self.kwargs['book_pk'])
        return HttpResponseRedirect(reverse_lazy('book_detail', args=[book.pk]))

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'books/review_delete.html'

    def get_success_url(self):
        return reverse_lazy('book_detail', args=[self.kwargs['book_pk']])
