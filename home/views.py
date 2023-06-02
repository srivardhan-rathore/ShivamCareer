from django.shortcuts import render, HttpResponse, get_object_or_404
from . import forms
from .models import College, Course


def home(request):
    colleges = College.objects.all()
    courses = Course.objects.all()
    context = {'colleges': colleges, 'courses': courses}
    return render(request, 'home/index.html', context)


def aboutus_page(request):
    return render(request, 'home/about-us.html')


def college_detail(request, uid):
    college = get_object_or_404(College, id=uid)
    context = {'college': college}
    return render(request, 'home/college_detail.html', context)


def contact_page(request):
    return render(request, 'home/contact-us.html')


def college_page(request):
    college = College.objects.all()
    courses = Course.objects.all()
    context = {'colleges': college, 'courses': courses}
    return render(request, 'home/college_page.html', context)


def contact_form(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(200)
    context = {'form': form}
    return render(request, 'home/contact.html', context)




