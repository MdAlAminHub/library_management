from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import status
from .models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):  
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
# For BOOK QUERY
def get_queryset(self):
    queryset = super().get_queryset() 
    author_name = self.request.query_params.get('author',None)
    genre = self.request.query_params.get('genre',None)
    start_date = self.request.query_params.get('start_date',None)
    end_date = self.request.query_params.get('end_date',None)


    if author_name : 
        queryset =queryset.filter(author_name__icontains =author_name )
    if genre : 
        queryset =queryset.filter(genre__icontains =genre ) 
    if start_date and end_date : 
        queryset =queryset.filter(published_date_range =[start_date,end_date ] )    

    return queryset

