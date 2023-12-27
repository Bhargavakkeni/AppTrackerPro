from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoginDetails
from .forms import LoginForm
from .serializers import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging
# Create your views here.

logging.basicConfig(level=logging.INFO, format="%(asctime)s-[%(levelname)s] [%(threadName)s] (%(module)s):%(lineno)d %(message)s",
                    filename='logging.log')

def index(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')


@api_view(['GET', 'POST', 'PUT'])
def signOn(request):
    if request.method == 'GET':
        mydict = {}
        if request.GET:
            username = request.GET['username']
            logins = LoginDetails.objects.filter(username = username).values()
            password = request.GET['password']
            for login in logins:
                if username == login['username'] and password == login['password']:
                    return redirect(f'app/{username}')
                else:
                    mydict['error'] = True
            return render(request, 'login.html', context=mydict)
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        mydict={}
        if LoginDetails.objects.filter(username=request.POST['username']).exists():
            logging.debug('Username already existed.')
            return render(request, 'register.html', {'exist':True})
        try:
            serializer = LoginSerializer(data=request.data)
        except Exception as e:
            mydict['error'] = True
            logging.debug('Error occured while saving login details: error {}, recieved data {}'.format(e,request.data))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return render(request, 'register.html',{'verify':True})
        else:
            mydict['error'] = True
            return render(request, 'register.html', context=mydict)

        
def app(request, *args, **kwargs):
    username = kwargs['username']
    mydict = {
        'username': username,
    }
    if username == 'admin':
        return render(request,'admin.html',context=mydict)
    else:
        return render(request,'user.html',context=mydict)
    

'''
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mydict ={'error':False}
        obj = LoginDetails(username=username, password=password)
        if obj:
            obj.save()
            mydict['verify'] = True
        else:
            mydict['error'] = True
        return render(request,'register.html',context=mydict)
    else:
        
        return render(request, 'register.html')
'''