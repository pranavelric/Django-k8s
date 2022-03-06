from pyexpat import model
from statistics import mode
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)