from django.db import models
from ckeditor.fields import RichTextField


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    description = RichTextField(max_length=5000, blank=True)

    def __str__(self):
        return self.name


class SubCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = RichTextField(max_length=5000, blank=True)


class College(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100)
    course_offered = models.ManyToManyField(Course)
    logo = models.ImageField(upload_to="college/logo/")
    image = models.ImageField(upload_to="college/image/")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    education_level = models.CharField(max_length=30)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=25)
    current_college = models.CharField(max_length=80)
    review = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)




