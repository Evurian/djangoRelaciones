from django.contrib import admin
from .models import Author, Book, Course, Student

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)