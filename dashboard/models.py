from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Email(models.Model):
    email_field = models.EmailField(max_length=254, blank=False, null=False)
    date_field = models.DateTimeField(auto_now_add=True)
    state_field = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.email_field
