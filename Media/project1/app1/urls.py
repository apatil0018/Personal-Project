from django.urls import path
from app1.views import StudentView, ShowStudentView,indexView

urlpatterns = [
    path('std/', StudentView, name='student_url'),
    path('ss/', ShowStudentView, name='ss_url'),
    path('pg/',indexView)
    
]