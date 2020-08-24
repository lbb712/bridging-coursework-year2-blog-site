from django.shortcuts import render, redirect
from django.http import HttpResponse
from cveditor.models import Item

# Create your views here.
def cv_edit(request):
    if request.method == 'POST':
        Item.objects.create(text = request.POST['item_text'] )
        return redirect('/cvedit/the_only_CV_in_the_world/')
    
    return render(request, 'cveditor/cv_edit.html')
    
def view_cv(request):
    items = Item.objects.all()
    return render(request, 'cveditor/cv_view.html', {'items': items})