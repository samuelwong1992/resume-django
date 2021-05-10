from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Project
from api.serializers import ProjectSerializer

@api_view(('GET',))
def get_all_projects(request) :
	projects = Project.objects.all()
	serializer = ProjectSerializer(projects, many=True, context={"request": request})
	return Response({'projects': serializer.data}, status=status.HTTP_200_OK)

@api_view(('GET',))
def get_project(request, pk) :
	project = get_object_or_404(Project, pk=pk)
	serializer = ProjectSerializer(project, many=False, context={"request": request})
	return Response({'project': serializer.data}, status=status.HTTP_200_OK)