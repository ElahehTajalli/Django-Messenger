from django.shortcuts import render
from users.models import Users
from message.models import Messages
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.

def chat(request, user_id=None):
    message = Messages.objects.filter(
        Q(receiver = user_id,
        sender = request.COOKIES.get('id'))|Q(receiver = request.COOKIES.get('id'),sender = user_id)
    )

    users = Users.objects.exclude(
        token = request.COOKIES.get('token')
    )

    return render(
        request,
        'chat.html',
        context={
           'users' : users,
           'receiver' : user_id,
           'messages' : message,
        }
    )


def add_message(request):
    m = Messages(
        text=request.POST['text'],
        sender=request.COOKIES.get('id'),
        receiver=request.POST['receiver']
    )
    m.save()
    message = Messages.objects.filter(
        Q(receiver = request.POST['receiver'],
        sender = request.COOKIES.get('id'))|Q(receiver = request.COOKIES.get('id'),
        sender = request.POST['receiver'])
    )
    users = Users.objects.exclude(
        token = request.COOKIES.get('token')
    )
    return render(
        request,
        'chat.html',
        context={
           'users' : users,
           'receiver' : request.POST['receiver'],
           'messages' : message,
        }
    )    
