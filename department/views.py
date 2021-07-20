from django.shortcuts import render,redirect
from .forms import DepartmentForm
from django .shortcuts import render,redirect
from .forms import DepartmentForm,ReportForm
from .models import Department,Report
from public.forms import PublicForm
# Create your views here.


def create_department(request):
    if request.method == 'GET':
        context = {
           'form':DepartmentForm()
        }
        return render(request,'create_department.html',context)
    else:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'create_department.html',{'form': form})


def report_create(request):
    if request.method=='GET':
        context = {
            'form':ReportForm()
        }
        return render(request,'create_report.html',context)
    else:
        form = ReportForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            c = Department.objects.get(user_id = request.user.id)
            data.Department = c
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'create_report.html',{'form':form})



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
              return redirect('dashboard',)
            else:
                return render(request,'create_public.html',{'form':form})
