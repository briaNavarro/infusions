from django.db import models
import re
import bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):

    def register(self, postData):
        my_hash = bcrypt.hashpw(
            postData['password'].encode(), bcrypt.gensalt()).decode()

        print('Making User.... ')
        return self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=my_hash)

    def authenticate(self, email, password):
        # return true/false to varify email
        same_email = self.filter(email=email)
        if not same_email:
            return False
        user = same_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def validate(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name needs 2 or more character'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name needs 2 or more character'

        if len(postData['email']) < 1:
            errors['email'] = 'Email required'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email'

        if len(postData['password']) < 2:
            errors['password'] = '8 characters or more for a password'

        if postData['password'] != postData['conf_password']:
            errors['password'] = 'Passwords dont match'

        same_email = self.filter(email=postData['email'])
        if same_email:
            errors['email'] = 'Email is taken'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}, || {self.last_name}, || {self.email},  || id: {self.id}'

    objects = UserManager()
