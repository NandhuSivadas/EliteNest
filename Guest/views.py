from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.


def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        ownercount=tbl_owner.objects.filter(owner_email=email,owner_password=password).count()

        
        if usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('webuser:homepage')
        elif admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('webadmin:homepage')
        
        elif ownercount > 0:
            ownerdata=tbl_owner.objects.get(owner_email=email,owner_password=password)
            request.session['oid']=ownerdata.id
            return redirect('webowner:homepage')
       
       
        else:
            msg="Invalid credentials!!"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')
    

def userregistration(request):
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("txt_gender")
        address=request.POST.get("txt_address")  
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        password=request.POST.get("txt_password")
        tbl_user.objects.create(user_name=name,user_contact=contact,user_email=email,user_gender=gender,user_address=address,user_photo=photo,user_proof=proof,user_password=password)


        return redirect('webguest:login')
    else:

        return render(request,'Guest/UserRegistration.html')

def ownerregistration(request):
    if request.method == "POST" and request.FILES:
        name = request.POST.get("txt_name")
        contact = request.POST.get("txt_contact")
        email = request.POST.get("txt_email")
        gender = request.POST.get("txt_gender")
        address = request.POST.get("txt_address")
        photo = request.FILES.get("txt_photo")
        proof = request.FILES.get("txt_proof")
        password = request.POST.get("txt_password")

        house_ids = request.POST.getlist("txt_house")  # Fetch house IDs as a list

        owner = tbl_owner.objects.create(
            owner_name=name,
            owner_contact=contact,
            owner_email=email,
            owner_gender=gender,
            owner_address=address,
            owner_photo=photo,
            owner_proof=proof,
            owner_password=password,
        )

        if house_ids:  # If houses were selected
            houses = tbl_house.objects.filter(id__in=house_ids)
            owner.houses.set(houses)  # Use set() for ManyToMany relationships

        return redirect('webguest:login')
    else:
        return render(request, 'Guest/OwnerRegistration.html')

def home_page(request):
    return render(request,'Guest/Homepage.html')    