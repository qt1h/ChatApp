from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    publication_date=models.DateTimeField('date plubished')
    def published_this_week(self):
        if self.publication_date>= (timezone.now()-datetime.timedelta(days=7)):
            return True
        else:
            return False
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username