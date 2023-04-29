from django.db import models
from users.models import CustomUser

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    date_created = models.DateField(null=True , blank=True)
    def __str__(self):
        return self.title
    
    
class TodoItem(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(null=True , blank=True)
    todo = models.ForeignKey(Todo , on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title