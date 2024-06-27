from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    available_copies = models.IntegerField(default=0)
    

    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def __str__(self):
        return self.title
    
    
class BorrowRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-borrow_date']
        verbose_name = 'Borrow Record'
        verbose_name_plural = 'Borrow Records'
        
    
    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title} on {self.borrow_date}"