from django.contrib import admin

from .models import College, Course, SubCourse, Contact


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias', 'address', 'logo', 'image')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name',)
    search_fields = ('name',)


@admin.register(SubCourse)
class SubCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name',)
    list_filter = ('course',)
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'course',
        'message',
        'created_at',
    )
    list_filter = ('course', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
