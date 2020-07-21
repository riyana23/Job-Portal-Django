from django.views.generic import TemplateView


class AboutPage(TemplateView):
    template_name = 'about.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

