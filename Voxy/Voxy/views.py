from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def help(request):
    return render(request, './help.html')