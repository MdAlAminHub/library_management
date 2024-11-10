from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register ( 'authors', AuthorViewSet)
router.register ( 'books', BookViewSet)



urlpatterns = [
    path ('', include (router.urls))
    # path('books/cached', AuthorListView.as_view(), name='list-authors'),

    # path('authors/', AuthorListView.as_view(), name='list-authors'),
    # path('books/', BookListView.as_view(), name='list-books'),

  
]