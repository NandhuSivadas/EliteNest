from django.urls import path,include
from Owner import views
app_name="webowner"

urlpatterns = [
    path('HomePage/',views.home_page,name='homepage'),

    path('MyProfile/',views.myprofile,name='myprofile'),
    path('EditProfile/',views.editprofile,name='editprofile'),
    path('ChangePassword/',views.changepassword,name='changepassword'),

    
    path('AddHouse/',views.add_house,name='add_house'),
    path('AddHouseList/',views.add_houselist,name='add_houselist'),

    path('update_house/<int:did>',views.update_house,name='update_house'),
    path('delete_house/<int:did>',views.delete_house,name='delete_house'),

    path('Report/',views.report,name='report'),
    path('ResetStatus/<int:booking_id>/',views.reset_status, name='reset_status'),

    path('LogOut/',views.logout,name="logout"),



 
    
   
]
