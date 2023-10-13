from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, AuthorListView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView, BookRentedListView, BookAvailableListView, ReaderListView, ReaderCreateView, ReaderDeleteView, ReaderUpdateView, RegisterView


urlpatterns = [
    # path("", BookListView.as_view()),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('author_list/', AuthorListView.as_view(), name='author_list'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('author_delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('author_update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('book_index/', BookRentedListView.as_view(), name='book_index'),
    path('book_available/', BookAvailableListView.as_view(), name='book_available'),
    path('reader_list/', ReaderListView.as_view(), name='reader_list'),
    path('reader_create/', ReaderCreateView.as_view(), name='reader_create'),
    path('reader_update/<int:pk>/', ReaderUpdateView.as_view(), name='reader_update'),
    path('reader_delete/<int:pk>/', ReaderDeleteView.as_view(), name='reader_delete'),
    path('register/', RegisterView.as_view(), name='register'),

]