from . import views
from django.urls import path
urlpatterns = [
    path('',views.home, name='student-home'),
    path('course/',views.course,name='student-course'),
    path('student/', views.student_details,name='student-details')
]