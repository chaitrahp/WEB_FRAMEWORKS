
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import(
UserCreationForm,
 RegistrationForm,
 EditProfileForm,
 contactform
 )
#from django.http.response import HttpResponseNotAllowed
#from . forms import register
from django.contrib.auth.models import User

from .models import category,category1,category2,category3,category4
#from .models import category
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
# Create your views here.

def action(request):
    act=get_object_or_404(category)
    return render(request,'accounts/action.html',{'act':act})

def education(request):
    edu=get_object_or_404(category1)
    return render(request,'accounts/education.html',{'edu':edu})


def drama(request):
    drama=get_object_or_404(category2)
    return render(request,'accounts/dramabooks.html',{'drama':drama})


def fiction(request):
    fic=get_object_or_404(category3)
    return render(request,'accounts/fictionbooks.html',{'fic':fic})


def history(request):
    his=get_object_or_404(category4)
    return render(request,'accounts/history.html',{'his':his})

def cart(request):
    args={'user':request.user}
    return render(request,'accounts/cart.html',args)


def home(request):

	numbers=[1,2,3,4,5]
	name='abcd'
	args={'myname':name,'numbers':numbers}
    #cats=category.objects.all 
	return render(request,'accounts/home.html',args)
    #return render(request,'accounts/home.html',{'cats':cats})

def register(request):
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		#return response('Hi')
		
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('app1/home.html')
			return redirect('/accounts')
			#return render(request,'app1/home.html')

		else:
			return HttpResponseNotAllowed(['get','post'])


	else:
		form=RegistrationForm()

		args = {'form':form}
	return render(request, 'accounts/reg_form.html',args) 

@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)

@login_required 
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)

def contactus(request):
    if request.method == 'POST':
        conform=contactform(request.POST)

        if conform.is_valid():
            f=conform.save(commit=False)
            f.save()

            return redirect('/accounts/login')
        else:
            return redirect('/accounts/login')
    else:
        conform=contactform()
        args={'conform':conform}
        return render(request,'accounts/contact.html',args)

