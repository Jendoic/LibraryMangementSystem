from django.contrib import admin
from .models import Category, Book, BorrowRecord

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BorrowRecord)
