from datetime import date
from uuid import uuid4
from django.db import models
from users.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    isbn = models.UUIDField(default=uuid4, unique=True, editable=False)
    category = models.CharField(max_length=100) 
    availability_status = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='books/images/',blank=True,null=True)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.book.availability_status = False  
        else:
            self.book.availability_status = True  
        self.book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
