from django.db import models

class URL(models.Model):
	url = models.CharField(max_length = 200)
	title = models.CharField(max_length = 100)
	meta_desc = models.CharField(max_length = 200)
	meta_keyword = models.CharField(max_length = 100)
	
	def __unicode__(self):              # __unicode__ on Python 2
		return "url = "+self.url + ", title = " + self.title + ",\n meta_desc = " + self.meta_desc + ",\n meta_keyword = " + self.meta_keyword
# Create your models here.
