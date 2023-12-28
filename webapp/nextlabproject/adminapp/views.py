from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models

from .models import LoginDetails, AppDetails, TaskDetails
from .serializers import LoginSerializer, AppDetailsSerializer, TaskDetailsSerializer
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
    appDetails = AppDetails.objects.all().values()
    print('appDetails',type(appDetails))
    mydict['appDetails'] = appDetails
    if username == 'admin':
        return render(request,'admin.html',context=mydict)
    else:
        logging.info('Username is not admin returning user page.')
        try:
            tasksIdList = TaskDetails.objects.filter(username = username).values('tasksId')
            logging.info('fetching tasks id list {}'.format(tasksIdList))
        except Exception as e:
            logging.debug('Error occured while fetching tasks ids from tasksdetails table in app function {}'.format(e))
            return render(request, 'user.html', {'error':True})
        
        try:
            results = TaskDetails.objects.filter(username = username).aggregate(
                totalPoints = models.Sum('points'),
                tasksCompleted = models.Count('tasksId')
                )
        except Exception as e:
            logging.debug('Error occured while fetching user task Details {}'.format(e))
            return render(request, 'user.html', {'error':True})
        
        mydict['remainingTasks'] = len(appDetails) - results['tasksCompleted']
        if tasksIdList:
            logging.info('fetched list of tasksIds is {}'.format(tasksIdList))
            appDetails = list(appDetails)
            for i in tasksIdList:
                for j in appDetails:
                    if i['tasksId'] == j['id']:
                        appDetails.remove(j)
            mydict['appDetails'] = appDetails
        if results['totalPoints']:
            mydict['results'] = results
        else:
            results['totalPoints'] = 0
            mydict['results'] = results
        
        return render(request,'user.html',context=mydict)
    

    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def addApps(request,id='', *args, **kwargs):
    if request.method == 'POST':
        logging.info('Recieved app data in addApps post method {}'.format(request.data))
        try:
            serializer = AppDetailsSerializer(data=request.data)
        except Exception as e:
            logging.debug('Error occured while serializing the data {e}'.format(e))
            return render(request, 'admin.html',{'error':True})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return render(request, 'admin.html',{'verify':True})
        else:
            logging.debug('Error occured while saving the data {e}'.format(e))
            return render(request, 'admin.html',{'error':True})
    elif request.method == 'DELETE':
        try:
            appdetails = AppDetails.objects.all().get(pk=id)
        except Exception as e:
            logging.debug('Error while fetching appDetails with id {} in addApps delete request method'.format(id))
            return render(request, 'admin.html',{'error':True})
        if appdetails:
            appdetails.delete()
            return render(request, 'admin.html',{'verify':True})


@api_view(['GET', 'POST'])
def saveTasks(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            serializer = TaskDetailsSerializer(data=request.data)
        except Exception as e:
            logging.debug('Error occured while serialzing the data. Received data {} error {}'.format(request.data,e))
            return render(request, 'user.html', {'error':False})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return render(request, 'user.html', {'verify':True})
        else:
            logging.debug('Error while saving the data. Recieved data {}'.format(serializer.validated_data))
            return render(request, 'user.html', {'error':False})
