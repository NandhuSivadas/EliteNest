from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
# Create your views here.

def home_page(request):
    user=tbl_owner.objects.get(id=request.session['oid'])
    return render(request,'Owner/Homepage.html',{'user':user})


def myprofile(request):
    user=tbl_owner.objects.get(id=request.session['oid'])
    return render(request,'Owner/MyProfile.html',{'user':user})


def editprofile(request):
    user=tbl_owner.objects.get(id=request.session['oid'])
    if request.method=="POST":
        user.owner_name=request.POST.get("txt_name")
        user.owner_email=request.POST.get("txt_email")
        user.owner_contact=request.POST.get("txt_contact")
        user.owner_address=request.POST.get("txt_address")
        user.save()
        return render(request,'Owner/EditProfile.html',{'user':user})
    else:
        return render(request,'Owner/EditProfile.html',{'user':user})
       

  

def changepassword(request):
    user=tbl_owner.objects.get(id=request.session['oid'])
    if request.method=="POST":
        currentpass=request.POST.get("txt_currentpassword")
        if user.owner_password == currentpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass==conpass:
                user.owner_password=newpass
                user.save()
                msg="successfully"
                return render(request,'Owner/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'Owner/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Owner/ChangePassword.html',{'msg':msg})

    else:
        return render(request,'Owner/ChangePassword.html')
def add_house(request):
    Cdata = tbl_category.objects.all()
    
    if request.method == 'POST':
        owner = tbl_owner.objects.get(id=request.session['oid'])  # Get the owner based on the session
        
        # Create and save a new house object
        house = tbl_house.objects.create(
            house_title=request.POST['txt_title'],
            house_description=request.POST['txt_description'],
            house_category=tbl_category.objects.get(id=request.POST.get("select")),
            house_price=request.POST['txt_price'],
            house_image=request.FILES['txt_image'],
            house_location=request.POST['txt_location'],
            house_status=1,  # Assuming 1 is for active/available houses
            owner=owner  # Assign the owner correctly
        )

        return redirect('webowner:add_house')  # Redirect after adding the house

    return render(request, 'Owner/AddHouse.html', {'Data': Cdata})

def add_houselist(request):
    owner = request.session.get('oid')  # Get the owner ID from session
    # housesid=tbl_owner.objects.get(id=houses)
    # houses=tbl_house.objects.get(id=housesid)
    houses = tbl_house.objects.filter(owner=request.session["oid"])
    return render(request, 'Owner/AddHouseList.html', {'owner': owner, 'houses': houses})




def update_house(request,did):
   Cdata=tbl_category.objects.all()
   Hdata=tbl_house.objects.all()
   updata=tbl_house.objects.get(id=did)
   if request.method=="POST":
     title=request.POST.get("txt_title")
     description=request.POST.get("txt_description")
     price=request.POST.get("txt_price")
     image=request.FILES.get("txt_image")
     category=tbl_category.objects.get(id=request.POST.get("select"))
     location=request.POST.get("txt_location")
     updata.house_title=title
     updata.house_description=description
     updata.house_price=price
     updata.house_image=image
     updata.house_category=category
     updata.house_location=location
     updata.save()
     return redirect('webowner:add_houselist')
   else:
     return render(request,'Owner/AddHouse.html',{'udata':updata,'Data':Cdata,'Hdata':Hdata})
      

def delete_house(request,did):
   tbl_house.objects.get(id=did).delete()
   return redirect('webowner:add_houselist')





def report(request): 
    owner = tbl_owner.objects.get(id=request.session['oid'])  # Get logged-in owner
    houses = tbl_house.objects.filter(owner=owner)  # Get all houses owned by this owner
    
    # Filter bookings where house belongs to the owner and booking & payment are done
    bookings = tbl_booking.objects.filter(
        house__in=houses, 
        booking_status='1', 
        payment_status='1'
    )

    return render(request, 'Owner/Report.html', {'bookings': bookings})



def reset_status(request,booking_id):
    
        # Get the booking object by id
        booking = tbl_booking.objects.get(id=booking_id)

        # Reset booking_status and payment_status to default
        booking.booking_status = '0'
        booking.payment_status = '0'
        booking.save()

        # Redirect back to the house bookings list page
        return redirect('webowner:report')  # Assuming this is the URL name for the list page


def logout(request):
    del request.session["oid"]
    return redirect("webguest:homepage")