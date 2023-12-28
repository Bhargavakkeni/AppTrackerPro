from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('signOn', views.signOn, name='signOn'),
    path('app/<str:username>',views.app,name='adminhome'),
    path('register',views.register,name='register'),
    path('addApps',views.addApps,name='addApps'),
    path('saveTasks',views.saveTasks,name='saveTasks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)