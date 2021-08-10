from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User


class Todo(models.Model):  # search for more fieds options in django model fields documentation
    title = models.CharField(max_length=100)
    # blank means that accepts blanks values
    memo = models.TextField(blank=True)
    # auto add sets the exact creation time. Not editable for the user
    created = models.DateTimeField(auto_now_add=True)
    # null means that accepts nulls values
    datecompleted = models.DateTimeField(null=True, blank=True)
    # false means it does not ned to be specified by the user
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
