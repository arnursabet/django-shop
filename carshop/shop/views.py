from django.shortcuts import render
from .models import Battery, Order

def index(request):
  return render(request, 'shop/index.html')

def catalog(request):
  context = {
    'batteries': Battery.objects.all()
  }
  return render(request, 'shop/catalog.html', context)
def about(request):
  return render(request, 'shop/about.html')

def faq(request):
  return render(request, 'shop/faq.html')

def contacts(request):
  return render(request, 'shop/contacts.html')
