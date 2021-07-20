from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,DepartmentRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from public.models import Public
from department.models import Department
from django.contrib.auth.models import User


def signup(request):
  if request.method == 'GET':
      context = {
         'form': SignupForm()}
      return render(request, 'signup.html', context)
  else:
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect ('signin')
    else:
        context = {
                'form': form
            }
        return render(request, 'signup.html', context)


def signin(request):
    if request.method == "GET":
        return render(request,'signin.html')
    else:
      u = request.POST.get('username')
      p = request.POST.get('password')
      user = authenticate(username=u,password=p)
      if user is not None:
        login(request, user)
        r = whoareyou(request.user.id)
        if r == 1:
            return redirect('jobseekerdash')
        elif r == 2:
            return redirect('dashbaord')
        else:
            return redirect('who')
      else:
           return redirect ('signin')


@login_required(login_url='signin')
def jobseekerdash(request):
    r=whoareyou(request.user.id)
    if r == 0:
        return redirect('who')
    elif r == 2:
        return redirect('dashboard')
    else:
        if request.method == 'GET':
            a = User.objects.get(id=request.user.id)
            p = Public.objects.get(user_id=request.user.id)

            context = {
                'user': a,
                'public':p,
            }
            return render(request,'jobseekerdash.html',context)
        else:
            form = Public
            if form.is_valid():
                data = form.save(commit=False)
                a = Public.objects.get(user_id=request.user.id)
                data.jobseeker_id = a.id
                data.save()
                return redirect('jobseekerdash')
            return redirect('jobseekerdash')


@login_required(login_url='signin')
def dashboard(request):
    context = {
            'c':Department.objects.get(user_id=request.user.id),
            'p':Public.objects.get(user_id=request.user.id),
}
    return render(request,'dashboard.html',context)










def who(request):
  return render(request,'who.html')


def signout(request):
    logout(request)
    return redirect('signin')

def whoareyou(id):
    try:
        Public.objects.get(user_id=id)
        return 1
    except:
        try:
            Department.objects.get(user_id=id)
            return 2
        except:
            return 0


def register(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')



def department_register(request):
    if request.method == 'GET':
        context = {
            'form': DepartmentRegisterForm()
        }
        return render(request,'department_register.html',context)
    else:
        form = DepartmentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request,'department_register.html',{'form': form})





