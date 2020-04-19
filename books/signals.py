import logging
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from books.models import Book


@receiver(pre_save, sender=Book)
def book_save(sender, instance, updated_fields, **kwargs):
    print(f"{instance}")
    print(f"{updated_fields}")
