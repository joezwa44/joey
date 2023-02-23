from django.db import models

class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=225
    )
    email = models.CharField(
        'Email', blank=False, null=False, max_length=225
    )
    password = models.CharField(
        'Password', blank=False, null=False, max_length=225
    )
    token = models.CharField(
        'Token', blank=True, null=True, max_length=500, db_index=True
    )
    token_expires = models.DateTimeField(
        'Token Expiration Date', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Date', blank=True, auto_now=True
    )

    def __str__(self):
        return self.email