from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from accounts.models import UserAccount
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.TextField()
    image=models.ImageField(upload_to ='uploads/') 
    borrowing_price=models.DecimalField(decimal_places=2, max_digits=10)
    categories=models.ForeignKey(Category,related_name="book",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    book=models.ForeignKey(Book,related_name="borrow",on_delete=models.CASCADE)
    account=models.ForeignKey(UserAccount,related_name="borrow",on_delete=models.CASCADE)
    borrow_after_price=models.DecimalField(decimal_places=2, max_digits=10,null=True)
    borrow_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.book.name
    
class Comment(models.Model):
    book=models.ForeignKey(Book,related_name="comment",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    comment=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

