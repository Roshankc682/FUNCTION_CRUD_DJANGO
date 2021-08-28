from django.urls import path
from home.views import *

urlpatterns = [
    path('books/create',book_create,name="books-create"),
    path('books/<int:id>/update',book_update,name="books-update"),
    path('books/',book_list,name="books-list"),
    path('books/<int:id>/details',book_single,name="book-single"),
    path('books/<int:id>/delete',book_delete,name="book-delete"),
]
