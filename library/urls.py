from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, BorrowRecordViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'borrow-records', BorrowRecordViewSet,basename='borrow-record')

urlpatterns = [
    path('', include(router.urls)),
]
