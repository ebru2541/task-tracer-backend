from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    )
     
    title=models.CharField(max_length=64)
    content=models.TextField(null=True, blank=True)   
    is_done=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    priority=models.PositiveSmallIntegerField(choices=PRIORITY, default=3)

    def __str__(self):
        return self.title