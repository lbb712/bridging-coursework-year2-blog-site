from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cveditor.models import CV
from .forms import CVForm

# Create your views here.
def cv_edit(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance= cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('view_cv', pk=cv.pk)
    else:
        form = CVForm(instance=cv)
    return render(request, 'cveditor/cv_edit.html', {'form': form})
    
def view_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, 'cveditor/cv_view.html', {'cv': cv})
    
def new_cv(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('view_cv', pk=cv.pk)
    else:
        form = CVForm()
        
    return render(request, 'cveditor/cv_edit.html', {'form': form})
    
def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'cveditor/cv_list.html', {'cvs':cvs})