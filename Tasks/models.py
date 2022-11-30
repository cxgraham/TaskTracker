from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
            return errors
        email = postData['email']
        if User.objects.filter(email=email):
            errors['email'] = 'Email already in use'
            return errors
        if len(postData['password']) < 5: 
            errors['password'] = 'Password must be at least five characters'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Password  does not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Task(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    priority = models.IntegerField()
    user = models.ForeignKey(User, related_name = 'tasks', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Create your models here.
