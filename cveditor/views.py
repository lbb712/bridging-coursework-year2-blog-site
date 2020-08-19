from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cv_edit(request):
    return HttpResponse('<html><title>CV Editor</title></html>')