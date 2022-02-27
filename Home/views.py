from email.mime import image
from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Medical,Resume,QR
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.conf import settings
import random
import string
import datetime
import qrcode
import cv2


def makeQR(link,location):
    data = link
    img = qrcode.make(data)
    img.save(location)
    return img

def readImg(path):
    img=cv2.imread(path)
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    return val

def readCam():
    cap=cv2.VideoCapture(0) ##cap var is storing cv2.Videocapture() param is camera index try 0 or -1

    detector = cv2.QRCodeDetector()

    while True:
        _,img= cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        cv2.imshow("window",img)
    # check if there is a QRCode in the image
        if data:
            a=data
            break

        k= cv2.waitKey(1)
        if k ==27:
            break
            cap.release()
            cv2.destroy_all_windows()
        


    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
  
    return str(a)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def home(request):
    return render(request,'home/index.html')

def create(request):
    return render(request,'home/create.html')

def read(request):
    return render(request,'home/read.html')

def contact(request):
    return render(request,'home/contact.html')

def medical(request):
    return render(request,'home/medical.html')

def resume(request):
    return render(request,'home/resume.html')

def postContact(request):
    if request.method=="POST":
        user=request.user
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        sex=request.POST['sex']
        dob=request.POST['dob']
        address=request.POST['address']
        relation=request.POST['relation']
        workplace=request.POST['workplace']
        designation=request.POST['designation']
        link=request.POST['link']
        photo=request.FILES['myfile']
        slug="contact"+get_random_string(10)+get_random_string(10)
        
        contact= Contact(user=user,photo=photo,fname=fname,lname=lname,sex=sex,email=email,address=address,dob=dob,mobile=mobile,matrialStatus=relation,workplace=workplace,designation=designation,links=link,slug=slug)
        contact.save()
        qrLink="http://127.0.0.1:8000/contact/"+slug
        location='media/qr/'+slug+'.png'
        img=makeQR(qrLink,location)
        
        context={'img': location}
    return render(request,"home/getQR.html",context)
    

def postMedical(request):
    if request.method=="POST":
        user=request.user
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        sex=request.POST['sex']
       
        height=request.POST['height']
        weight=request.POST['weight']
        blood=request.POST['blood']
        disease=request.POST['disease']
        doctor=request.POST['doctor']
        history=request.POST['history']
        report=request.FILES['myfile']
        slug="mediacl"+get_random_string(10)+get_random_string(10)
        mediacl= Medical(user=user,report=report,fname=fname,lname=lname,sex=sex,email=email,mobile=mobile,height=height,weight=weight,bgroup=blood,problem=disease,doctor=doctor,history=history,slug=slug)
        mediacl.save()
        qrLink="http://127.0.0.1:8000/medical/"+slug
        location='media/qr/'+slug+'.png'
        img=makeQR(qrLink,location)
        
        context={'img': location}
    return render(request,"home/getQR.html",context)

def postResume(request):
    return HttpResponse("im in pR")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['password']

        # check for errorneous input
        if len(username)<5:
            messages.error(request, "username lenght is less than 5")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        # Create the user
        try:
            user= User.objects.get(username=username)

            messages.error(request, "Username already exists")
            return redirect('home')
        except User.DoesNotExist:
            try:
                user= User.objects.get(email=email)

                messages.error(request, "email already exists")
                return redirect('home')
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, pass1)
                

        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def seeContact(request,slug):
    cr=Contact.objects.filter(slug=slug).first()
    context={'cr': cr}
    return render(request,'home/seeContact.html',context)


def seeMedical(request,slug):
    cr=Medical.objects.filter(slug=slug).first()
    
    context={'cr': cr}
    return render(request,'home/seeMedical.html',context)


def seeResume(request,slug):
    return HttpResponse('he')

def postQR(request):
    if request.method=="POST":
        user=request.user
        photo=request.FILES['myfile']
        slug=get_random_string(10)+get_random_string(10)
        myQR=QR(user=user,image=photo,slug=slug)
        myQR.save()
        img=QR.objects.filter(slug=slug)
        path='media/'
        for i in img:
            path+=str(i.image)
        new=readImg(path)
        print(new)
        return redirect(new)

def postCam(request):
    link=readCam()
    return redirect(link)

