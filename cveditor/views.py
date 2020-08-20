from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cv_edit(request):
    return render(request, 'cveditor/cv_edit.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })