'''
comments
'''
from django.urls import path
from . import views

'''
comments
'''
urlpatterns = [
    path('assignment/', views.StudentAssignment.as_view(), name='student assignments')
]