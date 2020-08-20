from django.shortcuts import render, redirect
from django.http import HttpResponse
from cveditor.models import Item

# Create your views here.
def cv_edit(request):
    if request.method == 'POST':
        Item.objects.create(text = request.POST['item_text'] )
        return redirect('/cvedit')
    
    items = Item.objects.all()
    
    return render(request, 'cveditor/cv_edit.html', {'items': items})