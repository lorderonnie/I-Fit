from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse
from .models import Profile,Workouts
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateProfileForm,UserUpdateform,NewWorkPlanForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'exercise/home.html')

def landingpage(request):
    return render(request,'exercise/landingpage.html')
@login_required(login_url = '/accounts/login/')
def workout(request):
    current_user = request.user 
    workouts = Workouts.get_all_workouts()
    return render(request,'exercise/workout.html',{"workouts":workouts,"current_user":current_user})

@login_required(login_url = '/accounts/login/')
def healthfacts(request):
    return render(request,'exercise/healthfact.html')


@login_required(login_url = '/accounts/login/')
def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)

    return render(request,"profile/profile.html",{"profile":profile,"name":name})

def delete(request,id):
    current_user = request.user 
    workouts = Workouts.objects.get(id=id)
    workout = Workouts.delete(self                                                                                                                                                                                                                                                                                  )
    return redirect ('workout')

@login_required(login_url = '/accounts/login/')   
def updateprofile(request):
   
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        form1 = UserUpdateform(request.POST,instance=request.user)
        if form.is_valid() and form1.is_valid():
            form1.save() 
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        form1 = UserUpdateform(instance=request.user)
    return render(request,"profile/updateprofile.html",{"form":form,"form1":form1})

@login_required(login_url="/accounts/login/")
def logout(request):
  logout(request)
  return redirect('home')


@login_required(login_url = '/accounts/login/')
def workplan(request):
    if request.method=='POST':
        form = NewWorkPlanForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('workout')

    else:
        form = NewWorkPlanForm()
        
    return render(request,'exercise/workplan.html',{'form':form})


