from django.urls import path

from .views import BooksApiList

urlpatterns = [
  path('books/', BooksApiList.as_view(), name='books_api_list')
]
