from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowReferencesView.as_view(), name='reference_view'),

    path('author/', views.ShowAuthorListView.as_view()),
    path('genre/', views.ShowGenreListView.as_view()),
    path('language/', views.ShowLanguageListView.as_view()),
    path('series/', views.ShowBookSeriesListView.as_view()),
    path('pubhouse/', views.ShowPublishingHouseListView.as_view()),

    path('author/<int:pk>/', views.ShowAuthorByPkView.as_view()),
    path('genre/<int:pk>/', views.ShowGenreByPkView.as_view()),
    path('language/<int:pk>/', views.ShowLanguageByPkView.as_view()),
    path('series/<int:pk>/', views.ShowBookSeriesByPkView.as_view()),
    path('pubhouse/<int:pk>/', views.ShowPublishingHouseByPkView.as_view()),

    path('author/create/', views.CreateAuthorView.as_view()),
    path('genre/create/', views.CreateGenreView.as_view()),
    path('language/create/', views.CreateLanguageView.as_view()),
    path('series/create/', views.CreateBookSeriesView.as_view()),
    path('pubhouse/create/', views.CreatePublishingHouseView.as_view()),

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
