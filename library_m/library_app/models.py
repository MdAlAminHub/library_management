from django.db import models

class Author (models.Model):
    author_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.author_name

    class Meta:
        ordering = ('-id',)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    genre = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = "Books"
        verbose_name_plural = "Books"