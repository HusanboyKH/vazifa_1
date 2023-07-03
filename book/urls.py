from django.urls import path
from .views import (AllBookView,DetailBookView,CreateBookView,
                    UpdateBookView,DeleteBookView,DetailAuthorView,DeleteAuthorView,CreateAuthorView,UpdateAuthorView,AllAuthorView)
urlpatterns = [
    path('',AllBookView.as_view()),
    path('<int:book_id>',DetailBookView.as_view()),
    path('create/',CreateBookView.as_view()),
    path('update/<int:book_id>/',UpdateBookView.as_view()),
    path('delete/<int:book_id>/',DeleteBookView.as_view()),
    path('Author/<int:Author_id>/',DetailAuthorView.as_view()),
    path('Author/create/',CreateAuthorView.as_view()),
    path('Author/update/<int:Author_id>/',UpdateAuthorView.as_view()),
    path('Author/', AllAuthorView.as_view()),
    path('Author/delete/<int:Author_id>/', DeleteAuthorView.as_view()),

]