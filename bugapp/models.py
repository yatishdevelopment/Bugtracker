from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100) 
    created_by = models.ForeignKey(User, related_name='projects',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)

class Issue(models.Model):
    project = models.ForeignKey(Project,verbose_name="issues",on_delete=models.CASCADE)
    issue_name = models.CharField(max_length=200)
    issue_descr = models.CharField(max_length=500)
    assignee = models.ForeignKey(User,verbose_name="issues",on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='issues',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)