from django.shortcuts import render

def index(request):
    return render(request, "notification/index.html")

def room(request, room_name):
    return render(request, "notification/room.html", {"room_name": room_name})