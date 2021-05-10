from django.contrib import admin

from api.models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin) :
	list_display = ('__str__',)
	filter_horizontal = ('technologies',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin) :
	list_display = ('__str__',)

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin) :
	list_display = ('__str__',)

@admin.register(ProjectRepo)
class ProjectRepoAdmin(admin.ModelAdmin) :
	list_display = ('__str__',)