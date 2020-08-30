from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product
from django.http import HttpResponseRedirect

# Create your views here.


@login_required(login_url='/')
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin")
        else:
             products = Product.objects.all()
             return render(request, 'product.html', {'products':products})

    
    else:
        return redirect('product') 

@login_required(login_url='/')
def admin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
             user = User.objects.filter(is_superuser=False)
             return render(request, 'admin.html', {'user':user})
        else:
            return redirect('product')
     
      
    else:
         return redirect('admin')

    

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    # user = User.objects.all()
    if request.user.is_authenticated:
        if request.user.is_superuser:                                                   
            
            return redirect('admin')
        else:    
           return redirect('product')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
          if username == 'admin1' and password == '123456':
              auth.login(request, user)
              return redirect('admin/')
          else: 
            auth.login(request, user)
            return redirect('product')
          
        else:
             messages.error(request, "Invalid username and password.")
             return render(request, 'registration/login.html')
             
            

    return render(request, 'registration/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']
        dicti = {"username":username,"email":email}
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return render('registration/register.html',dicti)
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email already taken',dicti)
                 return render('registration/register.html',dicti)
            else:     
              user = User.objects.create_user(username=username,email=email,password=password)
              user.save()
              return render(request,'registration/login.html')
        else:
           messages.error(request, "PASSWORD DOESN'T MATCH.")
           return render(request,'registration/register.html',dicti)

    else:

        return render(request,'registration/register.html')

def add(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']
        dicti = {"username":username,"email":email}
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email already taken',dicti)
                 return HttpResponseRedirect(request.path_info)
            else:     
                 user = User.objects.create_user(username=username,email=email,password=password)
                 user.save()
                 #print("User Created")
                 return redirect('admin')
        else:
           messages.error(request, "PASSWORD DOESN'T MATCH.")
           return render(request,'add.html')

    else:

        return render(request, 'add.html')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('admin')

def update(request,id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        user.username=username
        user.email=email
        user.save()
        return redirect('admin')
     
    
    return render(request, 'update.html' ,{'user':user})

def search(request):
     if request.method=='POST':
        username=request.POST['username']
        if User.objects.filter(username= username).exists():
            user=User.objects.get(username=username)
            return render(request,'search.html',{'userinfo':user})
        else:
            messages.info(request,'Search didnt found')
            return render(request,'search.html')
     messages.info(request,'PLEASE put something ')      
     return render(request,'search.html')
    
    









