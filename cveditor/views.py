from django.shortcuts import render

# Create your views here.
def cv_edit(request):
    return render(request, 'cveditor/cv_edit.html')