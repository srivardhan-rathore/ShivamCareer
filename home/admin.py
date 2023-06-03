from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple

from .models import Course, SubCourse, College, Contact, Testimonial, Blog


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name',)
    search_fields = ('name',)


@admin.register(SubCourse)
class SubCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'description',)
    list_filter = ('course',)
    search_fields = ('name',)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple},
    }
    list_display = ('name', 'alias',)
    raw_id_fields = ('course_offered',)
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'education_level',
        'course',
        'created_at',
    )
    list_filter = ('course', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'current_college',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cover_image',
        'author',
        'slug',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('slug',)
    date_hierarchy = 'created_at'
