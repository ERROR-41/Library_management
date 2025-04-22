from rest_framework import viewsets, permissions
from .models import Book, Author, BorrowRecord
from .serializers import BookSerializer, AuthorSerializer, BorrowRecordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from library.paginations import BookPagination,AuthorPaination
from django_filters.rest_framework import DjangoFilterBackend

# ViewSet for Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super().get_permissions()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

# ViewSet for Author
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPaination
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super().get_permissions()

# ViewSet for BorrowRecord
class BorrowRecordViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BorrowRecord.objects.filter(member=self.request.user).select_related('book', 'member')
        return BorrowRecord.objects.none()  
    
    serializer_class = BorrowRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(member=self.request.user)
        book = instance.book
        book.availability_status = False
        book.save()
    
    def perform_destroy(self, instance):
        book = instance.book
        book.availability_status = True
        book.save()
        instance.delete()
        
        
# ViewSet for ReturnRecord
class ReturnRecordViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BorrowRecord.objects.filter(member=self.request.user, returned=False).select_related('book', 'member')
        return BorrowRecord.objects.none()

    serializer_class = BorrowRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save(returned=True)
        book = instance.book
        book.availability_status = True
        book.save()
    
        
        

# Custom token views for JWT authentication
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class CustomTokenRefreshView(TokenRefreshView):
    pass
