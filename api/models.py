from django.db import models


class CodePromo(models.Model):
    code = models.CharField(primary_key=True, max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()


# class Historique(models.Model):
#     code = models.ForeignKey(CodePromo)
#     name = models.F(max_length=50, default='')
#     time = models.DateTimeField()
