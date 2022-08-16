from django.shortcuts import render, get_object_or_404
from .models import Project,Blog

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'projects/blogPostHome.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project,id=project_id)
    context = {
        'project':project
    }
    return render(request,'projects/detail.html', context)

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')

    context = {
        'blogs':blogs
    }
    return render(request,'simpleBlogWebsiteClone/all_blogs.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'simpleBlogWebsiteClone':blog
    }
    return render(request, 'simpleBlogWebsiteClone/blog_detail.html', context)