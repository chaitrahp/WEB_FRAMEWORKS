from django.shortcuts import redirect, HttpResponse

def login_redirect(request):
    return redirect('/accounts/login')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return render(request,'accounts/home.html',{'form':form})

    else:
        form=UserCreationForm()

        args={'form':form}
        return render(request, 'accounts/reg_form.html',args)