from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create,name="create"),
    path('read/',views.read,name="read"),
    path('create/contact/',views.contact,name='contact'),
    path('create/medical/',views.medical,name='medical'),
    path('create/resume/',views.resume,name='resume'),
    path('postContact',views.postContact,name='postContact'),
    path('postMedical',views.postMedical,name='postMedical'),
    path('postResume',views.postResume,name='postResume'),
    path('postQR',views.postQR,name='postQR'),
    path('postCam',views.postCam,name='postCam'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('contact/<str:slug>',views.seeContact,name="seecontact"),
    path('medical/<str:slug>',views.seeMedical,name="seemedical"),
    path('resume/<str:slug>',views.seeResume,name="seeresume")


   
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)