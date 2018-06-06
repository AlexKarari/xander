from django.shortcuts import render
from .models import Image

# Create your views here.
def main(request):
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})
    

def about(request):
    project = Image.objects.all()
    return render(request, 'index.html', {"image": image})
