from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = 'simpleSocialMediaClone/test.html'

class LogoutPage(TemplateView):
    template_name = 'simpleSocialMediaClone/thanks.html'

class HomePage(TemplateView):
    template_name = 'simpleSocialMediaClone/blogPostHome.html'
"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)
"""