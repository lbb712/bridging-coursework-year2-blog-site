from django.shortcuts import render, redirect
from django.http import HttpResponse
from cveditor.models import Item, CV

# Create your views here.
def cv_edit(request):
    
    return render(request, 'cveditor/cv_edit.html')
    
def view_cv(request):
    items = Item.objects.all()
    return render(request, 'cveditor/cv_view.html', {'items': items})
    
def new_cv(request):
    cv_ = CV.objects.create()
    Item.objects.create(text=request.POST['item_text'], cv=cv_)
    return redirect('/cvedit/the_only_CV_in_the_world/')