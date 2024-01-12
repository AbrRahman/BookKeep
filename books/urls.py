from django.urls import path,include
from .views import book_details,borrow_book,return_book
urlpatterns = [
    path('book_details/<int:id>/', book_details,name="book_details"),
    path('borrow/<int:id>/', borrow_book,name="borrow_book"),
    path('return_book/<int:id>/', return_book,name="return_book"),
]
