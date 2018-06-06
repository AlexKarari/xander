from django.shortcuts import render
from .models import Image, Project

# Create your views here.
def main(request):
    image = Image.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', {"image": image, "project": project})
    
