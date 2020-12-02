from django.views.generic import TemplateView


class BannerView(TemplateView):
    template_name = "banner_page.html"
