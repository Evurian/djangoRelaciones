from django.urls import path
from .views import author_books, course_students, generate_pdf, send_test_email

urlpatterns = [
    path('author/<int:author_id>/', author_books, name='author_books'),
    path('course/<int:course_id>/', course_students, name='course_students'),
    path('pdf/', generate_pdf, name='generate_pdf'),
    path('send-email/', send_test_email, name='send_test_email'),
]
