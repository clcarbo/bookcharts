from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    passhash = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    date_joined = models.DateTimeField('date joined')

    def __str__(self):
        return self.username

class Comment(models.Model):
    text = models.CharField(max_length=200)
    poster_id = models.ForeignKey(User, models.PROTECT)
    post_date = models.DateTimeField('date posted')

    def __str__(self):
        return self.text
