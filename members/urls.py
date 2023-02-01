from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]




urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),    
]
urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('services/', views.servicespage, name='servicespage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('contact/', views.contactpage, name='contactpage'),

]
