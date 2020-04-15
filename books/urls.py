from django.urls import path, include

from books.views import (
  BookListView,
  BookDetailView,
  BookCreateView,
  BookUpdateView,
  BookDeleteView,
  SearchResultsView
  )

urlpatterns = [
  path('', BookListView.as_view(), name='book_list'),
  path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
  path('create/', BookCreateView.as_view(), name='book_create'),
  path('<uuid:pk>/edit', BookUpdateView.as_view(), name='book_update_view'),
  path('<uuid:pk>/delete/', BookDeleteView.as_view(), name='book_delete_view'),
  path('search/', SearchResultsView.as_view(), name='search_results'),
]
