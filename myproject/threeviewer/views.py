from django.shortcuts import render

def model_viewer(request):
    return render(request, 'model_viewer.html')
