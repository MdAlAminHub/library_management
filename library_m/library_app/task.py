from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Book

@shared_task


def archive_old_books():
    ten_years_ago = timezone.now () - timedelta(days= 365*10)
    books_to_archive = Book.objects.filter(published_date__lt= ten_years_ago, is_archived=False)
    books_to_archive.update(is_archived=True)
