
# Create your views here.
from django.views.generic.base import TemplateView
from django.shortcuts import render
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
        #context['data'] = request.POST.get('location')
        json_data = json.loads(data)
        lst =  json_data.get('data')
        context['data'] = lst

        return render(request, "labels.html", context)

class ResultPageView(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_list = [
"https://www.indeed.ca/cmp/The-Writers'-Exchange/jobs/Volunteer-Literacy-Mentor-9868b9476f67b296?q=%22Job+Type%3A+Volunteer%22&vjs=3",
"https://www.indeed.ca/cmp/Pacific-Immigrant-Resources-Society/jobs/Childcare-Assistant-Volunteer-2c901cc1c6ad278b?q=%22Job+Type%3A+Volunteer%22&vjs=3",
"https://www.indeed.ca/cmp/Pacific-Immigrant-Resources-Society/jobs/Ece-Childcare-Assistant-Volunteer-a70319ca8b7ed5e6?q=%22Job+Type%3A+Volunteer%22&vjs=3",
"https://www.indeed.ca/cmp/Youth-Unlimited-Street-Life-East-Vancouver/jobs/Volunteer-Youth-Worker-cf82d1452d0e3c75?q=%22Job+Type%3A+Volunteer%22&vjs=3"]
        context['url_list'] = url_list
        return context

