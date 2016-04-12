from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from sport_event.models import Events
class CommentManager(models.Manager):
	def all(self):
		return super(CommentManager,self).filter(active=True).filter(parent=None)
	def create_comment(self, user=None,text=None,path=None,event=None):
		if not path:
			raise ValueError ("Musi zawierać ścieżkę")
		if not user:
			raise ValueError ("Musi zawierać użytkownika")

		comment = self.model(
			user = user,
			path = path,
			text = text
		)
		if event is not None:
			comment.event = event
		comment.save(using=self._db)
		return comment

class Comment(models.Model):
	user = models.ForeignKey(User)
	parent = models.ForeignKey("self",null=True,blank=True)
	path = models.CharField(max_length=350)
	event = models.ForeignKey(Events,null=True,blank=True)
	text = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = CommentManager()

	class Meta:
		ordering = ['-timestamp']
			

	def __str__(self):
		return self.text[0:20]+" ..."

	@property
	def get_comment(self):
		return self.text
	
	@property
	def is_child(self):
		if self.parent is not None:
			return True
		else:
			return False

	def get_children(self):
		if self.is_child:
			return None
		else:
			return Comment.objects.filter(parent=self)



