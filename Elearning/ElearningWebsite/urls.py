"""Elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('simpleBlogWebsiteClone/', include('simpleBlogWebsiteClone.urls'))
"""
from django.urls import path
from .views import index,contact,courses,course_detail,english,math

urlpatterns = [
    path('ElearningIndex/',index, name="ElearningIndex"),
    path('ElearningContact/',contact, name="ElearningContact"),
    path('ElearningCourses/',courses, name="ElearningCourses"),
    path('ElearningCourseDetail/<int:course_id>/',course_detail, name="ElearningCourseDetail"),
    path('ElearningCourse/english/',english, name="ElearningCourseEnglish"),
    path('ElearningCourse/math/',math, name="ElearningCourseMath"),
]
