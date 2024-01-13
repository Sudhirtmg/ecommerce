from django.http import JsonResponse
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
def BASE(rq):
    return render(rq,'base.html')
def HOME(rq):
    banner=Banner.objects.all()
    slider=Slider.objects.all()
    main_category=Main_Category.objects.all()
    product=Product.objects.filter(section__name='Top Deals Of The Day')
    
    context={
        'slider':slider,
        'banner':banner,
        'main_category':main_category,
        'product':product,
    }
    return render(rq,'Main/home.html',context)
def PRODUCT_DETAIL(rq,slug):
    product=Product.objects.filter(slug=slug)
    if product.exists():
            product=Product.objects.filter(slug=slug)
    else:
         return redirect('error')

    context={
     'product':product,
  }
    return render(rq,'product/product_detail.html',context)

def ERROR(rq):
    return render(rq,'error/404error.html')

def MY_ACCOUNT(rq):
     return render(rq,'account/my_account.html')

def REGISTER(rq):
     if rq.method=='POST':
          first_name=rq.POST.get('first_name')
          last_name=rq.POST.get('second_name')
          username=rq.POST.get('username')
          prefecture=rq.POST.get('address')
          district=rq.POST.get('sub_address')
          email=rq.POST.get('email')
          password=rq.POST.get('password')
          confirm_password=rq.POST.get('confirm_password')
      
          if User.objects.filter(username=username).exists():
               messages.error(rq,'username is already exists')
               return redirect('login')
          if User.objects.filter(email=email).exists():
               messages.error(rq,'email is already exists')
               return redirect('login')
          user=User(
                    first_name=first_name,
                    last_name=last_name,
                    # prefecture=prefecture,
                    # district=district,
                    username=username,
                    email=email,
     
                    )
          user.set_password(password)
          user.save()
          return redirect('login')
     
def LOGIN(rq):
     if rq.method=='POST':
          username=rq.POST.get('username')
          password=rq.POST.get('password')
          user=authenticate(rq,username=username,password=password)
          if user is not None:
               login(rq,user)
               return redirect('home')
          else:
               messages.error(rq,'Email and Password is invalid !')
               return redirect('login')
          

@login_required(login_url='/accounts/login/')          
def PROFILE(rq):

     return render(rq,'profile/profile.html')


@login_required(login_url='/accounts/login/')
def PROFILE_UPDATE(rq):

     if rq.method == 'POST':
          first_name=rq.POST.get('first_name')
          last_name=rq.POST.get('last_name')
          username=rq.POST.get('username')
          email=rq.POST.get('email')
          password=rq.POST.get('password')
          user_id=rq.user.id

          user=User.objects.get(id=user_id)
          user.first_name=first_name
          user.last_name=last_name
          user.email=email
          user.username=username
          if password != None and password != "":
            user.set_password(password)
          user.save()
          messages.success(rq,'プロファイルをアップデートしました')
          return redirect('profile')
     
def ABOUT(rq):
     return render(rq,'Main/about.html')
def PRODUCT(rq):
     category=Category.objects.all()
     product=Product.objects.all()
     context={
          'category':category,
          'product':product,
     }
     return render(rq,'product/product.html',context)
 
def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})
	
	