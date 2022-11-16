from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm, BangloreForm, MumbaiForm, ChennaiForm
from .models import Banglore, Mumbai, Chennai
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_branch:
                login(request, user)
                return redirect('branchs')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required(login_url='login')
def admin(request):
    return render(request,'adminpage.html')

@login_required(login_url='login')
def branchs(request):
    return render(request,'branchs.html')

@login_required(login_url='login')
def banglore(request):
    form = BangloreForm()
    if request.method=='POST':
        form=BangloreForm(request.POST)
        form.save()
        return redirect('banglore')
    
    data=Banglore.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'banglore.html',context)

@login_required(login_url='login')
def mumbai(request):
    form = MumbaiForm()
    
    if request.method=='POST':
        form=MumbaiForm(request.POST)
        form.save()
        return redirect('mumbai')
    
    data=Mumbai.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'mumbai.html',context)

@login_required(login_url='login')
def chennai(request):
    form = ChennaiForm()
    if request.method=='POST':
        form=ChennaiForm(request.POST)
        form.save()
        return redirect('chennai')
    
    data=Chennai.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'chennai.html',context)

@login_required(login_url='login')
def adminbanglore(request):
    data=Banglore.objects.all()
    context={
        
        'data':data,
    }

    return render(request,'adminbanglore.html',context)

@login_required(login_url='login')
def adminmumbai(request):
    data=Mumbai.objects.all()
    context={
        
        'data':data,
    }

    return render(request,'adminmumbai.html',context)

@login_required(login_url='login')
def adminchennai(request):
    data=Chennai.objects.all()
    context={
        
        'data':data,
    }

    return render(request,'adminchennai.html',context)

@login_required(login_url='login')
def chart_banglore(request):
    product_over_line1=[]
    product_over_line2=[]
    product_over_line3=[]
    product_over_line4=[]
    product_over_line5=[]
    labels=[]

    for i in Banglore.objects.all():
        product_over_line1.append(i.line1)
        product_over_line2.append(i.line2)
        product_over_line3.append(i.line3)
        product_over_line4.append(i.line4)
        product_over_line5.append(i.line5)
        labels.append(datetime.strftime(i.date,'%d-%m-%Y'))

    context={
        'product_over_line1':product_over_line1,
        'product_over_line2':product_over_line2,
        'product_over_line3':product_over_line3,
        'product_over_line4':product_over_line4,
        'product_over_line5':product_over_line5,
        'labels':labels,
    }
    return render(request,'chart_banglore.html',context)

@login_required(login_url='login')
def chart_chennai(request):
    product_over_line1=[]
    product_over_line2=[]
    product_over_line3=[]
    product_over_line4=[]
    labels=[]

    for i in Chennai.objects.all():
        product_over_line1.append(i.line1)
        product_over_line2.append(i.line2)
        product_over_line3.append(i.line3)
        product_over_line4.append(i.line4)
        labels.append(datetime.strftime(i.date,'%d-%m-%Y'))

    context={
        'product_over_line1':product_over_line1,
        'product_over_line2':product_over_line2,
        'product_over_line3':product_over_line3,
        'product_over_line4':product_over_line4,
        
        'labels':labels,
    }
    return render(request,'chart_chennai.html',context)

@login_required(login_url='login')
def chart_mumbai(request):
    product_over_line1=[]
    product_over_line2=[]
    product_over_line3=[]
    
    labels=[]

    for i in Mumbai.objects.all():
        product_over_line1.append(i.line1)
        product_over_line2.append(i.line2)
        product_over_line3.append(i.line3)
       
        labels.append(datetime.strftime(i.date,'%d-%m-%Y'))

    context={
        'product_over_line1':product_over_line1,
        'product_over_line2':product_over_line2,
        'product_over_line3':product_over_line3,
    
        'labels':labels,
    }
    return render(request,'chart_mumbai.html',context)



@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')   

