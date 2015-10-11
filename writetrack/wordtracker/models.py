from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	user = models.ForeignKey(User,related_name="projects")
	project_name = models.CharField(max_length=100)
	start_date = models.DateTimeField(auto_now=False,auto_now_add=False)
	end_date = models.DateTimeField(auto_now=False,auto_now_add=False)

	def __str__(self):
		return self.project_name + " belongs to: " + str(self.user)

class Tracker(models.Model):
	user = models.ForeignKey(User)
	tracker_name = models.CharField(max_length=100)
	tracker_project = models.ForeignKey(Project,related_name="trackers",blank=True,null=True)
	goal_name = models.CharField(max_length=100)
	goal_date = models.DateTimeField(auto_now=False,auto_now_add=False)
	goal_value = models.IntegerField()
	current_words = models.IntegerField()

	#def __unicode__(self):
      #      return self.tracker_name + " belongs to: " + self.user
     
	def __str__(self):
		return self.tracker_name + " (belongs to: " + str(self.user) + ")"

class WordCount(models.Model):
	tracker = models.ForeignKey(Tracker,related_name="wordcounts")
	words_datetime = models.DateTimeField(auto_now=False,auto_now_add=False)
	words = models.IntegerField()

	def __str__(self):
		return str(self.words) + "  words, at: " + str(self.words_datetime)







