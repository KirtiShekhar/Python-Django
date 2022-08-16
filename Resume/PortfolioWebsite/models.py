from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='statics/img/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resumeDetails', kwargs={
                'project_id':self.id
        })

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogDetails', kwargs={
                'blog_id':self.id
        })