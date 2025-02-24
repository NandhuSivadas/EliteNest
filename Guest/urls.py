from django.urls import path,include
from Guest import views
app_name="webguest"

urlpatterns = [
    path('',views.home_page,name='homepage'),
    path('Login/',views.login,name='login'),
    path('UserRegistration/',views.userregistration,name='userregistration'),
    path('OwnerRegistration/',views.ownerregistration,name='ownerregistration'),


    
   
]
