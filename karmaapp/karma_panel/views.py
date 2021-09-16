from django.conf.urls import url
from django.db.models import base
from django.db.models.fields import EmailField, URLField
from django.db.models.fields.files import ImageField, ImageFieldFile
from django.http import request
from django.urls.resolvers import URLPattern
from .models import *
from .utils import *
import random
from django.shortcuts import render,redirect,get_list_or_404


# Create your views here.
def home(request):
    if 'email' in request.session:
        print("------------------------------->",request.session['email'])
        uid=user.objects.get(email=request.session['email'])
        return render(request, 'index.html',{'name':uid.email})
    else:
        return render(request, 'index.html')

def addproduct(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        if request.method=='POST':
            productname=request.POST['productname']
            productimg=request.FILES['productimg']
            brand=request.POST['brand']
            price=request.POST['price']
            Description=request.POST['Description']
            #cat_id=request.POST['cat_id']
            #cat_id=request.POST['cat_id']
            #pid=add_product.objects.get()
            #instance=add_product.save()
            #c_id=category_dtls.objects.get['cid']
            # instance=category_dtls.cid
            # instance=add_product.cat_id
            #cat_id.save()
            # instance.cat_id=request.category_dlts(id)
            # instance.save()
            productimg=productimg
            print("==============/n",productimg,"/n===================")
            pid=add_product.objects.create(productname=productname,brand=brand,price=price,Description=Description,productimg=productimg)    
            
            #productimg=add_product.objects.create(productimg=productimg)
            #pid=cat_id.save()
            msg="Product Added Successfully"
            return render(request, 'addproduct.html',{'uid':uid,'name':uid.email,'msg':msg,'pid':pid,'productimg':productimg})
        else:
            return render(request, 'addproduct.html',{'uid':uid,'name':uid.email})
    else:
        return render(request, 'login.html')


def register(request):
    
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            rpassword=request.POST['rpassword']
            if password==rpassword:
                uid=user.objects.create(email=email,password=password)
                print("==========\n",email,password,"\n==========")
                print("USER CREATED")
                msg="User Created"    
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password didn't match"
                return render(request, 'register.html',{'msg':msg})
        else:
            return render(request,'register.html')
        

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print("-------------------------------------------------------->\n",email,password,"\n=====================")
        uid=user.objects.filter(email=email,password=password)
        if uid:
            uid=user.objects.get(email=email)
            if email==uid.email and password==uid.password:
                request.session['uid']=uid.id
                request.session['email']=uid.email
                return render(request, 'index.html',{'name':email})
            else:
                msg="User not found"
                return render(request, 'login.html',{'msg':msg})
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['uid']
        del request.session['email']
        msg="Successfully logout"
        return render(request, 'login.html', {'msg':msg})
    else:
        return render(request, 'login.html')

def forgot_pwd(request):
    return render(request,'forgot_pwd.html')

def reset_pwd(request):
   #try:
        email=request.POST['email']
        print(type(email))
        print("----->>>>>>>>>",email)
        uid = user.objects.get(email =email)
        print("---->>>",uid)
        uid=user.objects.filter(email=email)
        print(uid)
        if uid:
            uid=user.objects.get(email=email)
            otp=random.randint(1111,9999)
            uid.otp=otp
            uid.save() # update
            sendmail("Forgot-password",'otp_template',email,{'otp':otp})
            return render(request,'reset_pwd.html',{'email':email})
        else:
            emsg="user  Does Not Exist"
        return render(request,'forgot_pwd.html',{'msg':emsg})    
    #except:
        emsg="user  Does Not Exist"
        return render(request,'forgot_pwd.html',{'msg':emsg})

def reset_page(request):
    email=request.POST['email']
    otp=request.POST['otp']
    newpassword=request.POST['password']
    repassword=request.POST['repassword']

    uid=user.objects.get(email=email)

    if uid:
        if uid.otp==otp and newpassword==repassword:
            uid.password=newpassword
            uid.save()
            return render(request,"login.html")
        else:
            return render(request, "forgot_pwd.html")
    else:
        return render(request, "forgot_pwd.html")
    
def editprofile(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        if request.method=='POST':
            status=[]
            #char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            lstnum=[1,2,3,4,5,6,7,8,9,0]
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            contact_no=request.POST['contact_no']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pincode=request.POST['pincode']

            for i in firstname:
                if  (ord(i) >=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122):
                #if i in char:
                    status.append(1)
                else:
                    status.append(0)
                    break
            
            for i in lastname:
                if (ord(i) >=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122):
                #if i in char:
                    status.append(1)
                else:
                    status.append(0)
                    break

            # uid.email=email
            # uid.save()

            for i in contact_no:
                if int(i) in lstnum:
                    status.append(1)
                else:
                    status.append(0)
                    break
            
            #uid.address=address
            #uid.save()

            for i in city:
                if (ord(i) >=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122):
                #if i in char:
                    status.append(1)
                else:
                    status.append(0)
                    break
            
            for i in state:
                if (ord(i) >=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122):
                #if i in char:
                    status.append(1)
                else:
                    status.append(0)
                    break
            
            for i in country:
                if (ord(i) >=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122):
                #if i in char:
                    status.append(1)
                else:
                    status.append(0)
                    break
                
            if len(pincode)==6:
                for i in pincode:
                    if int(i) in lstnum:
                        status.append(1)
                    else:
                        status.append(0)
                        break
              
                        
            print(status) 

            if 0 in  status:
                print("=======\n","Invalid Details","\n=======")
                msg="Invalid Details!"
                return render(request,'editprofile.html',{'msg':msg,'name':uid.email,'uid':uid})                
            else:
                uid.firstname=firstname
                uid.lastname=lastname
                uid.email=email
                uid.contact_no=contact_no
                uid.address=address                    
                uid.city=city
                uid.state=state
                uid.country=country
                uid.pincode=pincode
                uid.save()
                print("=======\n","Details Updated Successfully","\n=======")
                msg="Details Updated Successfully!"
                return render(request,'index.html',{'msg':msg,'name':uid.email,'uid':uid})        
        else:
            return render(request,'editprofile.html',{'uid':uid,'name':uid.email})
    else:
        return render(request,'login.html')
    
def category(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        get_product_id=add_product.objects.filter(id=pk)    
        data=add_product.objects.all()
        return render(request, 'category.html',{'data':data,'name':uid.email})
    else:
        return render(request, 'login.html')

def add_to_cart(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        get_product_id=add_product.objects.get(id=pk)
        print("=====================\n",get_product_id,"\n========================")
        if request.method=="POST":
            p_name=request.POST['productname']
            p_price=request.POST['price']
            print(f"name={p_name}\n price={p_price}")
            return render('category.html')
        return render(request, 'category.html')
        
def CartPage(request):
    # get_cart=Cart.objects.all()
    #return render(request, 'cart.html',{'cart':get_cart})
    return render(request, 'cart.html')