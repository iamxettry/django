from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('images/', views.images, name='images'),
    path('form/', views.form, name='form'),
    path('submitMyform/', views.submitMyform, name='submitMyform'),
    path('add/<int:a>/<int:b>', views.add ,name="add"),
    path('intro/<str:name>/<str:age>', views.intro ,name="intro"),
]