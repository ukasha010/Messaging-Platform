from django.db import models

# Create your models here.

class ChatModel(models.Model):
    sender = models.CharField(max_length=100 , default=None)
    message = models.TextField(null=True , blank=True)
    thread_name = models.CharField(max_length=50 , null=True , blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message