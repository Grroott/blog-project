from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import secrets

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100, verbose_name = "Post title")
	content = models.TextField(verbose_name = "Post content")
	date_posted = models.DateTimeField(default=timezone.now, verbose_name = "Date posted")
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "author")
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug ="%s-%s" %(slugify(self.title, allow_unicode=True), secrets.token_hex(10))
		return super(Post, self).save(*args, **kwargs)