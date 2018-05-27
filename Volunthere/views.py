
# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LabelPageView(TemplateView):
    template_name = "labels.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = dict()
        context['data'] = request.POST.get('location')

        return render(request, "labels.html", context)
