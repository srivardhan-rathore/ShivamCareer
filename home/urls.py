from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus_page, name='aboutus_page'),
    path('contact/', views.contact_page, name='contact_page'),

    path('colleges/', views.college_page, name='college_page'),
    path('college/<str:uid>/', views.college_detail, name='college_detail'),

    path('courses/', views.course_page, name='course_page'),

    path('blogs/', views.blog_page, name='blog_page'),
    path('blog/<str:slug>', views.blog_detail, name='blog_detail'),
]
