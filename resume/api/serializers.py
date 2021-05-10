from rest_framework import serializers
from django.conf import settings

from api.models import Technology, ProjectImage, Project, ProjectRepo

class TechnologySerializer(serializers.ModelSerializer) :
	class Meta: 
		model = Technology
		fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer) :
	class Meta: 
		model = ProjectImage
		fields = '__all__'

class RepoSerializer(serializers.ModelSerializer) :
	class Meta: 
		model = ProjectRepo
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer) :
	images = ProjectImageSerializer(many=True, read_only=True)
	technologies = TechnologySerializer(many=True, read_only=True)
	repos = RepoSerializer(many=True, read_only=True)

	class Meta: 
		model = Project
		fields = '__all__'