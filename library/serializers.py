from rest_framework import serializers
from .models import Book, Author, BorrowRecord
from users.models import User
from djoser.serializers import UserCreateSerializer
from datetime import datetime


# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'isbn','author_name','availability_status']
    
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),write_only=True)
    


# Borrow record serializer
class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'return_date','book_name']
    
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_name = serializers.CharField(source='book.title', read_only=True)
    
    def validate_return_date(self, value):
        if not value:
            raise serializers.ValidationError("Return date must be filled.")
        if value <= datetime.now().date():
            raise serializers.ValidationError("Return date cannot be in the past or today.")
        return value
    
    def validate(self, data):
        book = data.get('book')
        if book and not book.availability_status:
            raise serializers.ValidationError({"book": "This book is currently unavailable for borrowing."})
        return data
    


# User serializer (for JWT authentication)
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        
