import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(
      primary_key=True,
      default=uuid.uuid4,
      editable=False,
      db_index=True,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(blank=True)

    class Meta:
        permissions = [
          ('special_status', 'Can read all books',),
        ]

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse('book_update_view', kwargs={"pk": self.pk})

    def __str__(self):
      return self.title

class Review(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
  )
  book = models.ForeignKey(
    Book,
    on_delete=models.CASCADE,
    related_name='reviews'
  )
  review = models.CharField(max_length=255)
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  def __str__(self):
    return self.review

