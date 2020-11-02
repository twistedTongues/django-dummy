from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_references_list_view),
    path('genres/create/', views.create_genres_view),
    path('author/create/', views.create_author_view),
    path('series/create/', views.create_series_view),
    path('pubhouse/create/', views.create_pubhouse_view),
    path('languages/create/', views.create_languages_view),
    path('genres/update/<int:pk>/', views.update_genres_view),
    path('author/update/<int:pk>/', views.update_author_view),
    path('series/update/<int:pk>/', views.update_series_view),
    path('pubhouse/update/<int:pk>/', views.update_pubhouse_view),
    path('languages/update/<int:pk>/', views.update_languages_view),
    path('genres/delete/<int:pk>/', views.delete_genres_view),
    path('author/delete/<int:pk>/', views.delete_author_view),
    path('series/delete/<int:pk>/', views.delete_series_view),
    path('pubhouse/delete/<int:pk>/', views.delete_pubhouse_view),
    path('languages/delete/<int:pk>/', views.delete_languages_view),
    path('<str:title>/<int:ref_id>/', views.show_reference_by_pk_view),
]
