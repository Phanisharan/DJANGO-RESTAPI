from django.db import models
from uuid import uuid4

STATUS_OPTIONS = (
    ['pending', 'Pending'],
    ['in_progress', 'In Progress'],
    ['completed', 'Completed']
    )
 
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS_OPTIONS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

