from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Category, Image, UserForm,Subscription, Contact
from django.contrib.auth.models import User, auth
from myapp.forms import UserForm, ContactForm

from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    cats = Category.objects.all()
    image_ = Image.objects.all()



            # PAGINATION VIEW
    paginator = Paginator(image_,6)

    page_number = request.GET.get('page')


    # image = get_object_or_404(Image, pk=pk)
    # is_favourite = False

    # if image.favourite.filter(pk=request.user.pk).exists():
    #     is_favourite = True

    


    try:

     page_obj = paginator.page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(page_obj.num_pages)

   
  

   

   



    data = {'cats':cats,
    
            'page_obj':page_obj
            # 'is_favourite':is_favourite
            
            

    }


    return render(request,'home.html',data)





# def favourite(request, pk):

#     image = get_object_or_404(Image, pk=pk)

#     if image.favourite.filter(pk=request.user.pk).exists():
#         image.favourite.remove(request.user)
#     else:
#         image.favourite.add(request.user)



#     return HttpResponseRedirect('home')


@login_required
def user_logout(request):
   logout(request)
   return redirect('/')


def category(request,cid):

   cats = Category.objects.all()

   category = Category.objects.get(pk=cid)

   page_obj = Image.objects.filter(cat=category)
   data = {'page_obj': page_obj,'cats':cats}
   return render(request,'home.html',data)





def signup(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
       

        if  user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,'Successfully registered!!!')
            return redirect('myapp:user_login')

           
            registered = True

            
        else:
            messages.warning(request,user_form.errors)

    else:
        user_form = UserForm()
       
    return render(request,'signup.html', {'user_form': user_form,'registered':registered})#'profile_form': profile_form,})






def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                messages.warning(request,'Account not active')
                return redirect('myapp:user_login')
        else:
            messages.warning(request,'Invalid credential ')
            return redirect('myapp:user_login')
    else:
        return render(request,'signin.html',{})



def pricing(request):


    
    daam = Subscription.objects.all()
    
    data = {'daam': daam}

    return render(request,'pricing.html',data)





def checkout(request,pk):
   
    price = get_object_or_404(Subscription, pk=pk)

    

    return render(request, 'checkout.html',{'price':price})







def aboutus(request):
    return render(request, 'about_us.html')



def privacy_policy(request):
    return render(request, 'privacy_policy.html')



def terms_of_use(request):
    return render(request, 'terms_of_use.html')


def agreement(request):
    return render(request,'agreement.html')


def contactus(request):
    is_contacted = False

    if request.method == 'POST':

        contact_form = ContactForm(data = request.POST)
       

        if  contact_form.is_valid():

            contact = contact_form.save()
            contact.save()
            messages.success(request,'Your Query has been submitted!!!')
            return redirect('myapp:contactus')

           
            is_contacted = True

            
        else:
            messages.warning(request,"Something went wrong")

    else:
        contact_form = ContactForm()
       
    

    return render(request,'contact_us.html', {'contact_form': contact_form,'is_contacted':is_contacted})
    



def thanks(request):
    return render(request, 'thanks.html')



def user_profile(request):
   

    

    return render(request,'user_profile.html')
