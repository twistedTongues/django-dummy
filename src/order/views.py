# Create your views here.
from django.views import generic
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from cart import models as cart_model


class OrderUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart = cart_model.Cart.objects.filter(pk=cart_id).first()
        return cart.order
