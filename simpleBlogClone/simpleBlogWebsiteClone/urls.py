"""simpleBlogClone URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/',auth_views.LoginView.as_view,name="login"),
    path('accounts/logout/',auth_views.LogoutView.as_view,name="logout"),
    path('postList/',views.PostListView.as_view(),name='postList'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='postDetail'),
    path('post/new/', views.CreatePostView.as_view(), name='postNew'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='postEdit'),
    path('drafts/', views.DraftListView.as_view(), name='postDraftList'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='postRemove'),
    path('post/<int:pk>/publish/', views.post_publish, name='postPublish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='addCommentToPost'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='commentApprove'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='commentRemove'),
]
