from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120, help_text='title of message.')
	message = models.TextField(help_text="what's on your mind ... ")

	def _str_(self):
		return self.title