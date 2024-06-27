from django.shortcuts import render
from .models import Category, Book, BorrowRecord
from .serializers import CategorySerializer, BookSerializer, BorrowRecordSerializer
from .paginations import BookPagination
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date


class CategoryViewSet(viewsets.ViewSet):
    permission_classesn = [IsAuthenticated]

    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except category.DoesNotExist:
            return Response({'error':'Category Not Found'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({"Message":f"{category.name} has been deleted"},status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({'error':'Category Not Found'},status=status.HTTP_404_NOT_FOUND)
 
    

class BookViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author']
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializer.errors:
    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        
    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({'message':f"{book.title} has been deleted"},status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
class BorrowRecordViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        if self.request.user.is_staff:
            borrow_record = BorrowRecord.objects.all()
        else:
            borrow_record = BorrowRecord.objects.filter(user=request.user)
        serializer = BorrowRecordSerializer(borrow_record, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def retrieve(self, request, pk=None):
        try:
            if self.request.user.is_staff or self.request.user:
                borrow_record = BorrowRecord.objects.get(pk=pk)
                serializer = BorrowRecordSerializer(borrow_record)
                return Response(serializer.data)
            raise PermissionDenied("You do not have permission to perform this request")
        except BorrowRecord.DoesNotExist:
            return Response({'error':'Borrow Record Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        
    def update(self, request, pk=None):
        try:
            if self.request.user.is_staff:
                borrow_record = BorrowRecord.objects.get(pk=pk)
                serializer = BorrowRecordSerializer(borrow_record, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            raise PermissionDenied("You do not have permission to perform this request")
        except BorrowRecord.DoesNotExist:
            return Response({'error':'Borrow Record Not Found'},status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def overDue(self, request):
        
        if self.request.user.is_staff:
            over_due = BorrowRecord.objects.filter(is_returned=False, return_date__lt=date.today())
            serializer = BorrowRecordSerializer(over_due, many=True)
            return Response(serializer.data)
        raise PermissionDenied("You do not have permission to perform this request")
    
        
    