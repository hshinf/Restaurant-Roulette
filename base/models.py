from django.db import models

class Restrandom(models.Model):
    name = models.CharField(max_length=50)
    visit_count = models.IntegerField(default=0)