from django.shortcuts import render
from .models import Member
# Create your views here.
from django.http import HttpResponse
from django.template import loader


def members(request):
    return HttpResponse("Hello world!")
    


def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,  
  }
  return HttpResponse(template.render(context, request))


# def homepage(request):
#   template = loader.get_template('webapp/home.html')
#   return HttpResponse(template.render())

def homepage(request):
  context = {'selected_page': 'home'}
  return render(request, 'webapp/home.html', context)


# def servicespage(request):
#   template = loader.get_template('webapp/services.html')
#   return HttpResponse(template.render())

def servicespage(request):
  context = {'selected_page': 'services'}
  return render(request, 'webapp/services.html', context)

# def aboutpage(request):
#   template = loader.get_template('webapp/about.html')
#   return HttpResponse(template.render())

def aboutpage(request):
  context = {'selected_page': 'about'}
  return render(request, 'webapp/about.html', context)

# def contactpage(request):
#   template = loader.get_template('webapp/contact.html')
#   return HttpResponse(template.render())
def contactpage(request):
  context = {'selected_page': 'contact'}
  return render(request, 'webapp/contact.html', context)