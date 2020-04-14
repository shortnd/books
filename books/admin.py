from django.contrib import admin

from books.models import Book, Review

class ReviewInline(admin.TabularInline):
  model = Review
class BookAdmin(admin.ModelAdmin):
  def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    is_superuser = request.user.is_superuser
    disabled_fields = set()

    if not is_superuser:
      disabled_fields |= {
        'price',
      }

    for f in disabled_fields:
      if f in form.base_fields:
        form.base_fields[f].disabled = True

    return form
  inlines = [
    ReviewInline
  ]
  list_display = ('title', 'author', 'price',)

admin.site.register(Book, BookAdmin)
