from django.db import models
from django.conf import settings


# Create your models here.

# class Book(models.Model):
#     
# 
# class Chart(models.Model):


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post_date = models.DateTimeField('date posted')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             default="")

    def __str__(self):
        return self.text
