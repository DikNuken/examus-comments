# Create your views here.
from django.views.generic.base import TemplateView


class ExampleView(TemplateView):
    template_name = 'example/example.html'
