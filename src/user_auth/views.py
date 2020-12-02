from django.contrib.auth import views, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


from . import forms


class MyLoginView(views.LoginView):
    pass


class MyLogoutView(views.LogoutView):
    """
    A view that logout user and redirect to homepage.
    """
    permanent = False
    query_string = True
    pattern_name = 'home'
    template_name = 'registration/logout.html'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(MyLogoutView, self).get_redirect_url(*args, **kwargs)


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = '/account/login'
    template_name = 'registration/registration.html'


class MyResetPasswordView(views.PasswordResetView):
    template_name = 'registration/reset_password.html'


class MyResetPasswordDoneView(views.PasswordResetDoneView):
    template_name = 'registration/reset_password_done.html'


class MyAccountView(LoginRequiredMixin, views.TemplateView):
    template_name = 'my_account.html'
