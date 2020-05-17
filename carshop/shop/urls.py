from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('catalog', views.catalog, name='catalog'),
  path('faq', views.faq, name='faq'),
  path('contacts', views.contacts, name='contacts')
]
