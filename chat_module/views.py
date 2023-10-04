from django.shortcuts import render


def index(request):
    return render(request, 'chat_module/index.html')


def room(request, room_name):
    context = {
        'room_name': room_name
    }
    return render(request, 'chat_module/room.html', context)
