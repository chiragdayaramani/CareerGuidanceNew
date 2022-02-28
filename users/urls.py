from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views as users_views

from django.conf.urls import include,url
urlpatterns = [
    path('', users_views.home,name='home'),
    path('signup/',users_views.signup,name='signup'),
    path('login/',users_views.login,name='login'),
    # path('logout/',users_views.logout,name='logout'),
    path('after10/', users_views.after10, name='after10'),
    path('after12arts/', users_views.after12arts, name='after12arts'),
    path('after12science/', users_views.after12science, name='after12science'),
    path('after12commerce/', users_views.after12commerce, name='after12commerce'),
    path('about/', users_views.about, name='about'),
    path('contact/', users_views.contact, name='contact'),
    path('feedbackform/', users_views.feedbackform, name='feedbackform'),
    path('after10colleges/', users_views.after10colleges, name='after10colleges'),
    path('after12engcolleges/', users_views.after12engcolleges, name='after12engcolleges'),
    path('after12medicolleges/', users_views.after12medicolleges, name='after12medicolleges'),
    path('after12commcolleges/', users_views.after12commcolleges, name='after12commcolleges'),
    path('after12artscolleges/', users_views.after12artscolleges, name='after12artscolleges'),
    path('after10result/', users_views.after10result, name='after10result'),
    path('after12artsresult/', users_views.after12artsresult, name='after12artsresult'),
    path('after12commresult/', users_views.after12commresult, name='after12commresult'),
    path('after12sciresult/', users_views.after12sciresult, name='after12sciresult'),

  
]