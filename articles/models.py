from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
  # Those Fields can be found on the documentation
  title = models.CharField(max_length = 100)
  slug  = models.SlugField()
  body  = models.TextField()
  date  = models.DateTimeField(auto_now_add = True)
  thumb = models.ImageField(default = 'default.png', blank = True)
  author = models.ForeignKey(User, on_delete=None, default=None)

  # python3 manage.py makemigrations
  # python3 manage.py migrate

  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[:50] + '...'