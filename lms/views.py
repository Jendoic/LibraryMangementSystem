from django.shortcuts import render
from .models import Category, Book, BorrowRecord
from .serializers import CategorySerializer, BookSerializer, BorrowRecordSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes


class CategoryViewSet(viewsets.ViewSet):
    
    def list(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    

class BookViewSet(viewsets.ViewSet):
    
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
        except book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        
    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
class BorrowRecordViewSet(viewsets.ViewSet):
    
    def list(self, request):
        borrow_record = BorrowRecord.objects.filter(user=request.user)
        serializer = BorrowRecordSerializer(borrow_record, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        