from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_references_list_view),

    path('author', views.ShowAuthorListView.as_view()),

    # path('genres/create/', views.create_genres_view),
    # path('authors/create/', views.create_author_view),
    # path('seriess/create/', views.create_series_view),
    # path('pubhouses/create/', views.create_pubhouse_view),
    # path('languages/create/', views.create_languages_view),
    # path('genres/update/<int:pk>/', views.update_genres_view),
    # path('authors/update/<int:pk>/', views.update_author_view),
    # path('seriess/update/<int:pk>/', views.update_series_view),
    # path('pubhouses/update/<int:pk>/', views.update_pubhouse_view),
    # path('languages/update/<int:pk>/', views.update_languages_view),
    # path('genres/delete/<int:pk>/', views.delete_genres_view),
    # path('authors/delete/<int:pk>/', views.delete_author_view),
    # path('seriess/delete/<int:pk>/', views.delete_series_view),
    # path('pubhouses/delete/<int:pk>/', views.delete_pubhouse_view),
    # path('languages/delete/<int:pk>/', views.delete_languages_view),
    path('author/create/', views.CreateAuthorView.as_view()),
    path('genre/create/', views.CreateGenreView.as_view()),
    path('language/create/', views.CreateLanguageView.as_view()),
    path('series/create/', views.CreateBookSeriesView.as_view()),
    path('pubhouse/create/', views.CreatePublishingHouseView.as_view()),

    path('<str:title>/<int:ref_id>/', views.show_reference_by_pk_view),

    path('author/update/<int:pk>/', views.UpdateAuthorView.as_view()),
    path('genre/update/<int:pk>/', views.UpdateGenreView.as_view()),
    path('language/update/<int:pk>/', views.UpdateLanguageView.as_view()),
    path('series/update/<int:pk>/', views.UpdateBookSeriesView.as_view()),
    path('pubhouse/update/<int:pk>/', views.UpdatePublishingHouseView.as_view()),

    path('author/delete/<int:pk>/', views.DeleteAuthorView.as_view()),
    path('genre/delete/<int:pk>/', views.DeleteGenreView.as_view()),
    path('language/delete/<int:pk>/', views.DeleteLanguageView.as_view()),
    path('series/delete/<int:pk>/', views.DeleteBookSeriesView.as_view()),
    path('pubhouse/delete/<int:pk>/', views.DeletePublishingHouseView.as_view()),
]
