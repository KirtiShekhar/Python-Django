from django.shortcuts import render,get_object_or_404
from .models import Project,Service,TeamMember
from .forms import ProjectFilter

# Create your views here.
def index(request):
    services = Service.objects.all()
    teammembers = TeamMember.objects.all()
    context = {
        'services':services,
        'teammembers':teammembers
    }
    return render(request, 'blogPostHome.html', context)

def all_projects(request):
    projects = Project.objects.all()
    filtered = ProjectFilter(request.GET, queryset=projects)
    projects = filtered.qs

    context = {
        'projects':projects,
        'filtered':filtered
    }
    return render(request, 'all_projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project':project
    }
    return render(request, 'project_detail.html', context)