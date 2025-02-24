from datetime import datetime
import random
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q

from User.models import *
from Admin.models import *
from Guest.models import *

# Create your views here.

def homepage(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Homepage.html',{'user':user})
   

def myprofile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'user':user})
  

def editprofile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        user.user_name=request.POST.get("txt_name")
        user.user_email=request.POST.get("txt_email")
        user.user_contact=request.POST.get("txt_contact")
        user.user_address=request.POST.get("txt_address")
        user.save()
        return redirect('webuser:myprofile')
    else:
        return render(request,'User/EditProfile.html',{'user':user})
       

  

def changepassword(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        currentpass=request.POST.get("txt_currentpassword")
        if user.user_password == currentpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass==conpass:
                user.user_password=newpass
                user.save()
                msg="successfully"
                return render(request,'User/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'User/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'User/ChangePassword.html',{'msg':msg})

    else:
        return render(request,'User/ChangePassword.html')
    

def review(request):
   if request.method=="POST":
      tbl_review.objects.create(review=request.POST.get("txt_review"))
      return redirect("webuser:review")
   else:
      return render(request,'User/Review.html')


def houselist(request):
    # Get IDs of houses that are booked and paid for
    booked_and_paid_houses = tbl_booking.objects.filter(
        booking_status='1', 
        payment_status='1'
    ).values_list('house_id', flat=True)

    # Get houses that are NOT booked and paid for
    available_houses = tbl_house.objects.exclude(id__in=booked_and_paid_houses)

    # Render the available houses to the template
    return render(request, 'User/HouseList.html', {'Data': available_houses})




def search_houses(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        price = request.GET.get('price')
        houses = tbl_house.objects.all()

        if price:
            houses = tbl_house.objects.filter(house_price=price)
        
        house_data = list(houses.values(
            'house_title', 'house_description', 'house_location', 'house_price', 'house_image'
        ))

        # Construct full URL for image field
        for house in house_data:
            house['image_url'] = house['house_image']  # This should be the correct URL

        return JsonResponse({'houses': house_data})
    else:
        houses = tbl_house.objects.all()
     
        context = {
            'Data': houses,
            
        }
        return render(request, 'HouseList.html', context)




def booking(request, did):
    house = tbl_house.objects.get(id=did)  # Get the house instance using did
    user = tbl_user.objects.get(id=request.session['uid'])  # Get the user from session
    
    # Create a new booking
    tbl_booking.objects.create(
        booking_amount=house.house_price,  # Use the house instance's price
        user=user,  # Assign the user instance
        house=house,  # Assign the house instance, not its id
        booking_status=1
    )
    
    return redirect('webuser:mybooking')


def mybooking(request):
    userid=request.session['uid']
    booking=tbl_booking.objects.filter(user=userid)
    return render(request,'User/MyBookings.html',{'Data':booking})

def paymentticket(request,id):
   booking=tbl_booking.objects.get(id=id)
   amount=booking.booking_amount
   if request.method=="POST":
      booking.payment_status=1
      booking.save()
      return redirect("webuser:loader")
   else:
    return render(request,"User/Payment.html",{'amnt':amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def cancelbooking(request,id):
    booking=tbl_booking.objects.get(id=id)
    booking.status= 3
    booking.save()
    return redirect("webuser:viewmyticket")


def logout(request):
    del request.session["uid"]
    return redirect("webguest:homepage")