from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.username
    
