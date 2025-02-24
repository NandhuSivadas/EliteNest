from django.urls import path,include
from User import views
app_name="webuser"

urlpatterns = [
    path('HomePage/',views.homepage,name='homepage'),
    path('Review/',views.review,name='review'),
    path('HouseList/',views.houselist,name='houselist'),

    path('MyProfile/',views.myprofile,name='myprofile'),
    path('EditProfile/',views.editprofile,name='editprofile'),
    path('ChangePassword/',views.changepassword,name='changepassword'),

    path('MyBookings/',views.mybooking,name='mybooking'),
    path('Booking/<int:did>',views.booking,name='booking'),

    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

    path('paymentticket/<int:id>',views.paymentticket,name='paymentticket'),
    path('cancelbooking/<int:id>',views.cancelbooking,name="cancelbooking"),


     path('LogOut/',views.logout,name="logout"),
     path('search/', views.search_houses, name='search_houses'),




 





   

    
   
]
