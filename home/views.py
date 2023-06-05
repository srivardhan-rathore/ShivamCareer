from django.shortcuts import render, HttpResponse, get_object_or_404
from . import forms
from .models import College, Course, Blog, Testimonial, Contact
import threading
from django.conf import settings
from django.core.mail import EmailMessage


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

        email_subject = f'New query: {contact.name}: {contact.email}'
        email_message = f'Name: {contact.name} \nMessage: {contact.message}' \
                        f' \nEmail: {contact.email} \nPhone: {contact.phone}' \
                        f' \nEducation: {contact.education_level} \nCourse: {contact.course}'
        EmailThread(email_subject, email_message, ["shivamcareerconsultancy@gmail.com"]).start()
        return render(request, 'home/contact-success.html')
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home/contact-us.html', context)


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


def course_detail(request, uid):
    course = get_object_or_404(Course, id=uid)
    colleges = College.objects.filter(course_offered=course)
    testimonials = Testimonial.objects.all()
    context = {'course': course, 'colleges': colleges, 'testimonials': testimonials}
    return render(request, 'home/course_detail.html', context)


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


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(self.subject, self.html_content, settings.DEFAULT_FROM_EMAIL,
                               self.recipient_list)
        message.content_subtype = "html"
        print(message.send(fail_silently=False))

        print(message.to)



