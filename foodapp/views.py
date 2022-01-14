from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Food

from .models import Comment
from .models import Profile

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



from django.template import loader

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,'foodapp/index.html')

def about(request):
    return HttpResponse('<h1>Thsi is the about page</h1>')
def contact(request):
    return HttpResponse('<h1>Thsi is the contact page</h1>')
def tracker(request):
    return HttpResponse('<h1>Thsi is the tracker page</h1>')


def cart(request):
    all_foods = Food.objects.all()
    all_users = User.objects.all()
    all_profiles = Profile.objects.all()
    
    length = len(all_foods)
    context = {
        'all_foods':all_foods,
        'length':length,
        'all_users':all_users,
        'all_profiles':all_profiles
        
    }
    return render(request,'foodapp/cart.html',context)
def prodView(request):
    
    all_foods = Food.objects.all()
    length = len(all_foods)
    
    context = {

        'all_foods':all_foods,
        'length':length
    }
    
    return render(request,'foodapp/prod1.html',context)
def confirmView(request):
    
    all_foods = Food.objects.all()
    length = len(all_foods)
    
    context = {

        'all_foods':all_foods,
        'length':length
    }
    
    return render(request,'foodapp/confirmation.html',context)

@login_required
def profile(request):
    
    all_foods = Food.objects.all()
    length = len(all_foods)
    
    context = {

        'all_foods':all_foods,
        'length':length
    }
    
    return render(request,'foodapp/profile.html',context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()   
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    
    return render(request,'foodapp/update.html',context)



def track(request):
    
    all_foods = Food.objects.all()
    length = len(all_foods)
    
    context = {

        'all_foods':all_foods,
        'length':length
    }
    
    return render(request,'foodapp/maps.html',context)

def prodIndian(request):
    
    all_foods = Food.objects.all()
    length = len(all_foods)
    
    context = {

        'all_foods':all_foods,
        'length':length
    }
    
    return render(request,'foodapp/prodIndian.html',context)

def detail(request,name):

    

    all_foods = Food.objects.all()
    all_comments = Comment.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect(cart)
    else:
        form = UserRegisterForm()
    
    context = { 

            'all_foods':all_foods,
            'name':name,
            'all_comments':all_comments,
            
        }
    return render(request,'foodapp/detail.html',context)
'''
def register(request):

    

    all_users = User.objects.all()

       

        
    context = {

            'all_users':all_users,
            
            
        }
    return render(request,'foodapp/register.html',context)
'''    
'''    
def add(request):

    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    foodp = request.POST['foodp']

    new_user = User(u_fname = fname,u_lname = lname,u_username = username,u_password = password,u_email = email,u_address = address,u_foodp = foodp)    

    new_user.save()





    return redirect(register)
'''
'''
def add(request):

    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    foodp = request.POST['foodp']

    all_users = User.objects.all()
    count =0
    for user in all_users:
        if user.u_username != username:
            count = count +1 
            
            
            
        elif user.u_username==username and user.u_password==password:
            return redirect(prodView)
    return redirect(register)
'''   

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        address = request.POST['address']
        phone = request.POST['phone']
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            address = request.POST['address']
            phone = request.POST['phone']
            new_profile = Profile(address = address,phone = phone)
            
            user_obj = User.objects.get(username=username)
             
            new_profile.person = user_obj

            new_profile.save()


            
            return redirect(prodView)
    return render(request,'foodapp/register2.html',{'form':form})
    
def add_comment(request):

    ctext = request.POST['ctext']
    name = request.POST['name']
    food = request.POST['food']
    all_foods = Food.objects.all()
  
            
    new_comment = Comment(text = ctext)
    food_obj = Food.objects.get(item_name=food)
    user_obj = User.objects.get(username=name)
    new_comment.food = food_obj  
    new_comment.name = user_obj

    new_comment.save()





    return redirect('/shop/productview/'+food)

    

    
    





    

