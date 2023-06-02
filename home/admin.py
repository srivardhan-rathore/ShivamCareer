from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple

from .models import Course, SubCourse, College, Contact, Testimonial, Blog


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description')
    search_fields = ('name',)


@admin.register(SubCourse)
class SubCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'description')
    list_filter = ('course',)
    search_fields = ('name',)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple},
    }
    list_display = ('id', 'name', 'alias', 'address', 'logo', 'image')
    raw_id_fields = ('course_offered',)
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'education_level',
        'course',
        'message',
        'created_at',
    )
    list_filter = ('course', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'current_college',
        'review',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'cover_image',
        'author',
        'content',
        'slug',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('slug',)
    date_hierarchy = 'created_at'
