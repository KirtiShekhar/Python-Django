from django.db import models
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='statics/img/new_service/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='statics/img/newteam/')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=30)
    TYPE = (
            ('Office', 'Office'),
            ('Residential', 'Residential'),
            ('Commercial', 'Commercial')
        )
    type = models.CharField(max_length= 50, null=True, choices=TYPE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='statics/img/newproject/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('interiorDesignProjectDetails', kwargs = {
                'project_id':self.id
        })
