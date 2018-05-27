
# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View
import json

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
        data = open('labels.json').read()
        context = dict()
        context['data'] = request.POST.get('location')
        context['json_data'] = json.dumps(data)
        return render(request, "labels.html", context)
