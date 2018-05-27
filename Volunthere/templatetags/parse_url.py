from django import template

register = template.Library()
import re

@register.filter
def parse_url_org(url):

    res = re.search("https:\/\/www.indeed.ca\/cmp\/(.*?)\/jobs\/(.*?)\?", url)
    return res.group(1)

@register.filter
def parse_url_id(url):
    res = re.search("https:\/\/www.indeed.ca\/cmp\/(.*?)\/jobs\/(.*?)\?", url)
    return res.group(2)