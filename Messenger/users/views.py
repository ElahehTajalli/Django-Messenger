from django.shortcuts import render,redirect
from users.models import Users
from django.http import HttpResponse
import uuid



# Create your views here.

def validate_user_add_request(data):
    if len(data['password']) < 2:
        return False, 'Your firstname must be greater than 3 chars', 'firstname'
 
    return True, ''



def user_add(request) :
    if request.method == 'POST':
        validate = validate_user_add_request(request.POST)
        if validate[0]:
            u = Users (
                firstname=request.POST['firstname'],
                lastname=request.POST['lastname'],
                username=request.POST['username'],
                password=request.POST['password'],
                avatar='https://',
                token=uuid.uuid4()
            )
            try:
                u.save()
            except:
                return HttpResponse(
                    "Duplicate",
                    status=400
                )
            response = redirect(
                '/chats/'
            )
            response.set_cookie('token', u.token)
            response.set_cookie('id', u.id)
            return response
        else:
            return HttpResponse("Error", status=400)

    elif request.method == 'GET':
        return render(
            request,
            'signUp.html'
        )



def login(request):
    if request.method == 'GET':
        return render(
            request,
            'login.html',
            context={
                'error': '',
            }
        )

    elif request.method == 'POST':
        user = Users.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user:
            user[0].token=uuid.uuid4()
            user[0].save()
            response = redirect(
                '/chats/'
            )
            response.set_cookie('token', user[0].token)
            response.set_cookie('id', user[0].id)
            return response
        else :
            return render(
                request,
                'login.html',
                context={
                    'error': 'Not Found'
                },
                status= 404
            )  
            





