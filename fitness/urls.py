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
    path('workout/',views.workout,name="workout"),
    path('healthfact/',views.healthfacts,name="healthfacts"),
    url(r'^workplan/',views.workplan,name='workplan'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



