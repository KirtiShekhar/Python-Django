from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title



class Course(models.Model):
    title = models.CharField(max_length=30)
    overview = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = models.TextField(max_length=200)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('ElearningCourseDetail', kwargs={
                'course_id':self.id
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    course=models.ForeignKey('Course', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email