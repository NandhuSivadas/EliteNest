from django.shortcuts import render,redirect

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from Admin.models import *
from Guest.models import *
from User.models import *

# Create your views here.
def home_page(request):
    return render(request,'Admin/Homepage.html')

def add_house(request):
    Cdata=tbl_category.objects.all()
    Hdata=tbl_house.objects.all()
    if request.method=="POST" and request.FILES:
     
     
     title=request.POST.get("txt_title")
     description=request.POST.get("txt_description")
     price=request.POST.get("txt_price")
     image=request.FILES.get("txt_image")
     category=tbl_category.objects.get(id=request.POST.get("select"))
     location=request.POST.get("txt_location")
     tbl_house.objects.create(house_title=title,house_description=description,house_category=category,house_image=image,house_price=price,house_location=location,admin=tbl_admin.objects.get(id=request.session["aid"]))
     return render(request,'Admin/AddHouse.html',{'Data':Cdata,'HouseData':Hdata})
    else:
       return render(request,'Admin/AddHouse.html',{'Data':Cdata,'HouseData':Hdata})

def add_houselist(request):
   Data=tbl_house.objects.all()
   return render(request,'Admin/AddHouseList.html',{'HouseData':Data})     
       
def category(request):
    Cdata=tbl_category.objects.all()
    if request.method=="POST":
       name=request.POST.get("txt_name")
       tbl_category.objects.create(category_name=name)
       return render(request,'Admin/Category.html',{'Data':Cdata})
    else:
        return render(request,'Admin/Category.html',{'Data':Cdata})

def categorylist(request):
   Cdata=tbl_category.objects.all()
   return render(request,'Admin/CategoryList.html',{'Data':Cdata})
      
       
def update_category(request,did):
   Cdata=tbl_category.objects.all()
   updata=tbl_category.objects.get(id=did)
   if request.method=="POST":
        name=request.POST.get("txt_name")
        updata.category_name=name
        updata.save()
        return redirect('webadmin:Category')
   else:
      return render(request,'Admin/Category.html',{'Data':Cdata,'udata':updata})
      
      
def delete_category(request,did):
   tbl_category.objects.get(id=did).delete()
   return redirect('webadmin:Category')

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
     return redirect('webadmin:add_house')
   else:
     return render(request,'Admin/AddHouse.html',{'udata':updata,'Data':Cdata,'Hdata':Hdata})
      

def delete_house(request,did):
   tbl_house.objects.get(id=did).delete()
   return redirect('webadmin:add_house')


def logout(request):
    del request.session["aid"]
    return redirect("webguest:homepage")

def ownerslist(request):
    owners = tbl_owner.objects.prefetch_related('tbl_house_set')  # Default related name
    owner_data = []

    for owner in owners:
        houses = owner.tbl_house_set.all()  # Use the default reverse relation name
        if houses.exists():
            for house in houses:
                owner_data.append({
                    'name': owner.owner_name,
                    'contact': owner.owner_contact,
                    'email': owner.owner_email,
                    'gender': owner.owner_gender,
                    'address': owner.owner_address,
                    'house_title': house.house_title,
                    'house_description': house.house_description,
                    'house_price': house.house_price
                })
        else:
            owner_data.append({
                'name': owner.owner_name,
                'contact': owner.owner_contact,
                'email': owner.owner_email,
                'gender': owner.owner_gender,
                'address': owner.owner_address,
                'house_title': "No House Registered",
                'house_description': "No House Registered",
                'house_price': "No House Registered"
            })

    return render(request, 'Admin/ownerslist.html', {'owners': owner_data})

    
    owners = tbl_owner.objects.all().prefetch_related('houses')
    owner_data = []

    for owner in owners:
        houses = owner.houses.all()  
        if houses.exists():
            for house in houses:
                owner_data.append({
                    'name': owner.owner_name,
                    'contact': owner.owner_contact,
                    'email': owner.owner_email,
                    'gender': owner.owner_gender,
                    'address': owner.owner_address,
                    'house_title': house.house_title,
                    'house_description': house.house_description,
                    'house_price': house.house_price
                })
        else:
    
            owner_data.append({
                'name': owner.owner_name,
                'contact': owner.owner_contact,
                'email': owner.owner_email,
                'gender': owner.owner_gender,
                'address': owner.owner_address,
                'house_title': "No House Registered",
                'house_description': "No House Registered",
                'house_price': "No House Registered"
            })

    return render(request, 'Admin/ownerslist.html', {'owners': owner_data})



def Report(request):
    paid_bookings = tbl_booking.objects.filter(payment_status="1")
    unpaid_bookings = tbl_booking.objects.filter(payment_status="0")
    return render(request,'Admin/Report.html',{'paid_bookings': paid_bookings, 'unpaid_bookings': unpaid_bookings})

