from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_book_list_view),
    path('book/<int:book_id>/', views.show_book_by_pk_view),
    path('book/create/', views.create_book_view),
    path('book/update/<int:pk>/', views.update_book_view),
    path('book/delete/<int:pk>/', views.delete_book_view),

]
