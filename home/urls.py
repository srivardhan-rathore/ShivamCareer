from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colleges/', views.college_page, name='college_page'),
    path('aboutus/', views.aboutus_page, name='aboutus_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('college/<str:uid>/', views.college_detail, name='college_detail'),
]
