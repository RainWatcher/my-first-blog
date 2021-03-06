from django.db import models
from django.utils import timezone

# Create your models here.
# This is defining the Database Table to store Blog Posts
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	# This describes how the record should be 'Printed' 
	def __str__(self):
		return self.title
