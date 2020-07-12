from django.db import models

class Widget(models.Model):
  description = models.CharField(max_length=200)
  quantity = models.CharField(max_length=10)
  def __str__(self):
    return self.name
