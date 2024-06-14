from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Author, Book, Course, Student
from .utils import render_to_pdf

def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_books.html', {'author': author, 'books': books})

def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'course_students.html', {'course': course, 'students': students})

def generate_pdf(request):
    context = {'data': 'Hello, PDF!'}
    pdf = render_to_pdf('pdf_template.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def send_test_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return render(request, 'email_sent.html')
