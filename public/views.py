from django.shortcuts import render,redirect
from .forms import Public
from django.shortcuts import render
from .forms import PublicForm
from django.contrib.auth.models import User
from onlinec.views import whoareyou
from department.forms import ReportForm
from department.models import Report,Department

# Create your views here.


def create(request):
    if request.method == 'GET':
            context = {
             'form': PublicForm()
            }

            return render(request,'create_public.html',context)
    else:
            form = PublicForm(request.POST,request.FILES or None)
            if form.is_valid():
              data = form.save(commit = False)#data is temporarely saved.
              data.user_id = request.user.id
              data.save()
              return redirect('jobseekerdash',)
            else:
                return render(request,'create_public.html',{'form':form})

def create_form(request):
    if request.method == 'GET':
            context = {
             'form': PublicForm()
            }

            return render(request,'create_public.html',context)
    else:
            form = PublicForm(request.POST,request.FILES or None)
            if form.is_valid():
              data = form.save(commit = False)#data is temporarely saved.
              data.user_id = request.user.id
              data.save()
              return redirect('dashboard',)
            else:
                return render(request,'create_public.html',{'form':form})









def report_list(request):
    c = Department.objects.get(user_id=request.user.id)
    context = {
        'report': Report.objects.filter(Department_id=c.id)

    }
    return render(request,'list_report.html',context)


