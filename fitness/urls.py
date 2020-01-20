from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='home'),
    path('fitness/profile/',views.profile,name="profile"),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),    
    path('logout/',views.logout,name = 'logout'),
    
    
    
]


