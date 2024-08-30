from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def first(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

def second(request):
  template = loader.get_template('second.html')
  return HttpResponse(template.render())

def third(request):
  template = loader.get_template('third.html')
  return HttpResponse(template.render())