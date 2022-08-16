"""advancedView URL Configuration

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
from .views import IndexView,SchoolListView,SchoolDetailView,SchoolCreateView,SchoolUpdateView,SchoolDeleteView

urlpatterns = [
    path('advancedView/',IndexView.as_view(),name='index'),
    path('advancedViewList/', SchoolListView.as_view(), name='list'),
    path('advancedViewList/<int:pk>/', SchoolDetailView.as_view(), name='detail'),
    path('create/', SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SchoolDeleteView.as_view(), name='delete')
]
