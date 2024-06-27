from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *



router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'books', BookViewSet, basename='books')
router.register(r'borrowedRecords', BorrowRecordViewSet, basename='borrowedRecords')


urlpatterns = [
    path('', include(router.urls)),
]