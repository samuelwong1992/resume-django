from django.db import models

from datetime import datetime
from os.path import splitext

def images_handler(instance, filename):
    """Image uploads custom handler."""
    today = datetime.today()

    return '{year}/{week}/{name}{ext}'.format(
        year=today.year,
        week=today.isocalendar()[1],
        name=today.strftime('%m%d%H%M%S%f'),
        ext=splitext(filename)[1].lower())

class Technology(models.Model):
	title = models.CharField(max_length=150)

	class Meta:
		verbose_name = 'Technology'
		verbose_name_plural = 'Technologys'

	def __str__(self):
		return self.title

class ProjectImage(models.Model):
	image = models.ImageField(upload_to=images_handler)
	project = models.ForeignKey("api.Project", verbose_name="project", related_name="images", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Project Image"
		verbose_name_plural = "Project Images"

	def __str__(self):
		return self.project.title

class ProjectRepo(models.Model):
	repo = models.CharField(max_length=150)
	project = models.ForeignKey("api.Project", verbose_name="repo", related_name="repos", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Project Repo"
		verbose_name_plural = "Project Repos"

	def __str__(self):
		return self.project.title

class Project(models.Model):
	title = models.CharField(max_length=150)
	roles = models.CharField(max_length=150)
	subtitle = models.CharField(max_length=150)
	value_proposition = models.TextField()
	contribution = models.TextField()
	technologies = models.ManyToManyField(Technology, verbose_name="technologies")
	thumbnail = models.ImageField(upload_to=images_handler, blank=True, null=True)

	class Meta:
		verbose_name = "Project"
		verbose_name_plural = "Projects"

	def __str__(self):
		return self.title
