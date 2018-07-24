from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+_-]+@[a-zA-z0-9+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name must be longer than 2 charaters"
        if len(postData['first_name']) > 255:
            errors["first_name"] = "First Name must be shorter than 255 charaters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = 'Last Name must be longer than 2 characters'
        if len(postData['last_name']) > 255:
            errors["last_name"] = 'Last Name must be shorter than 255 characters'
        if User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already taken"
        if len(postData['email']) < 8:
            errors["email"] = 'Email must be at least 8 characters long'
        if len(postData['email']) > 255:
            errors["email"] = 'Email must be at shorter than 8 characters long'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email not in email format'
        if len(postData['password']) < 8:
            errors["password"] = "Password must be 8 characters long"
        if len(postData['password']) > 255:
            errors["password"] = "Password must be shorter than 8 characters long"
        if postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors
        
    def create_user(self, postData):
        hash_pass = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = hash_pass,
        )
        return user

    def validateLogin(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['username'] = 'Email must be populated'
        if User.objects.filter(email=postData['email']).exists():
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = 'E-mail password combination is incorrect.'
        else:
            errors['mail'] = 'E-mail password combination is incorrect.'
        return errors

    def validateEdit(self,postData):
        errors = {}
        if len(postData['first']) < 1 :
            errors['first'] = "First name must be populated"
        if len(postData['first']) > 255 :
            errors['first'] = "First name must be less than 255 characters"
        if len(postData['first']) < 1 :
            errors['last'] = "Last name must be populated"
        if len(postData['last']) > 255 :
            errors['last'] = "Last name must be less than 255 characters"
        if User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already taken"
        if len(postData['email']) < 8:
            errors["email"] = 'Email must be at least 8 characters long'
        if len(postData['email']) > 255:
            errors["email"] = 'Email must be at shorter than 8 characters long'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email not in email format'
        return errors
        
class QuoteManager(models.Manager):
    def validateQuote(self, postData):
        errors = {}
        if len(postData['liveQuote']) < 10:
            errors['liveQuote'] = "Quote must be more than 10 characters"
        if len(postData['liveQuote']) > 255:
            errors['liveQuote'] = "Quote must not exceed 255 characters"
        if len(postData['author']) < 3:
            errors['author'] = "Author name must be more than 3 characters"
        if len(postData['author']) > 255:
            errors['author'] = "Author name must not exceed 255 characters"
        return errors

    # def create_quote(self, postData):
    #     quote = self.create(
    #         content = postData['liveQuote'],
    #         author = postData['author'],
    #         one = Quote.objects.get(id= postData['user_quote_id'])
    #     )
    #     return quote

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return "{} - {}".format(self.id, self.email)

class Quote(models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    one = models.ForeignKey(User, related_name="oneT")
    many = models.ManyToManyField(User, related_name="manyT")
    likes = models.ManyToManyField(User, related_name="likesT")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

    def __str__(self):
        return "{} - {}".format(self.id, self.content)