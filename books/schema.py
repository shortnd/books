import graphene
from graphene_django import DjangoObjectType

from .models import Book, Review
from graphql import GraphQLError

class BookType(DjangoObjectType):
    class Meta:
        model = Book


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class Query(graphene.ObjectType):
    books = graphene.List(
      BookType
    )
    reviews = graphene.List(
      ReviewType
    )

    def resolve_books(self, info, **kwargs):
      return Book.objects.all()

    def resolve_reviews(self, info, **kwargs):
      return Review.objects.all()

class CreateBook(graphene.Mutation):
  id = graphene.UUID()
  title = graphene.String()
  author = graphene.String()
  price = graphene.Float()

  def mutate(self, info, title, author, price):
    book = Book(
      title=title,
      author=author,
      price=price
    )

    return CreateBook(
      id=book.id,
      title=book.title,
      author=book.author,
      price=book.price,
    )

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
