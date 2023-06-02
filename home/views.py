from django.shortcuts import render, HttpResponse, get_object_or_404
from . import forms
from .models import College, Course, Blog, Testimonial, Contact


def home(request):
    colleges = College.objects.all()
    courses = Course.objects.all()
    testimonials = Testimonial.objects.all()
    context = {'colleges': colleges, 'courses': courses, 'testimonials': testimonials}
    return render(request, 'home/index.html', context)


def aboutus_page(request):
    return render(request, 'home/about-us.html')


def contact_page(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.education_level = request.POST.get('education_level')
        contact.course = request.POST.get('course')
        contact.message = request.POST.get('message')
        contact.save()

    return render(request, 'home/contact-us.html')


# College Page
def college_page(request):
    college = College.objects.all()
    courses = Course.objects.all()
    testimonials = Testimonial.objects.all()
    context = {'colleges': college, 'courses': courses, 'testimonials': testimonials}
    return render(request, 'home/college_page.html', context)


def college_detail(request, uid):
    college = get_object_or_404(College, id=uid)
    context = {'college': college}
    return render(request, 'home/college_detail.html', context)


def course_page(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home/course_page.html', context)


# Blog Page
def blog_page(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'home/blog_page.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog}
    return render(request, 'home/blog_detail.html', context)


def contact_form(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(200)
    context = {'form': form}
    return render(request, 'home/contact-us.html', context)




