from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>/", views.book_info, name="book_info"),
    path("new/", views.new_book, name="new_book"),
    path("<int:book_id>/delete", views.book_delete, name="book_delete"),
]
