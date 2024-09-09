from django.db import models
from projects.models import Project
from account.models import User


# Create your models here.
class Comment(models.Model):
    cotent = models.CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    review = models.CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Report(models.Model):
    reason = models.CharField(max_length=500)
    statues = models.CharField(max_length=5)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
