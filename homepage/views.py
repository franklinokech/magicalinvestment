from django.shortcuts import render


# Define method to handle request to index
def index(request):
    return render(request, 'homepage/index.html', {})
