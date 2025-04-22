from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5
  
class AuthorPaination(PageNumberPagination):
    page_size = 8