from django.contrib import admin

# Register your models here.
from wordtracker.models import Tracker
from wordtracker.models import Project
from wordtracker.models import WordCount

admin.site.register(Tracker)
admin.site.register(Project)
admin.site.register(WordCount)
