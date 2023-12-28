from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
def chatroom(request):
    return render(request, 'chatroom.html')