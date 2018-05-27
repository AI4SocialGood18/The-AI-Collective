from django.conf.urls import url
from Volunthere.views import HomePageView, LabelPageView
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url('labels', LabelPageView.as_view(), name='labels')
]