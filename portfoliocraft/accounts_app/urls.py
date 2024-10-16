from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [ 
path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('homepage/',views.Homepage,name='homepage'),
    path('logout/',views.logout,name='logout'),
    ]