from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    return HttpResponse("here are our projects")

def project(request, pk):
    return HttpResponse(f"SIngle Pojrect: {pk} ")