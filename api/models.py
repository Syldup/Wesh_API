from django.db import models
from django.contrib.auth.models import User


class CodePromo(models.Model):
    code = models.CharField(primary_key=True, max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()


class History(models.Model):
    code = models.ForeignKey(CodePromo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
