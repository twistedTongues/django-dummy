from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyAccountView.as_view(), name='myaccount'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('register/', views.SignUpView.as_view(), name="signup"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('reset_password/', views.MyResetPasswordView.as_view(),
         name='reset_password'),
    path('reset_password_done/', views.MyResetPasswordDoneView.as_view(),
         name='reset_password_done'),
]
