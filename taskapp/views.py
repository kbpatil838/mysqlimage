from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmpForm
from django.contrib.auth import get_user_model
User = get_user_model()

def emp_reg(request):

    # form = EmpForm(request.POST or None)
    # context = {
    #     'form':form
    # }
    if request.method == 'POST':
        form = EmpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp')
        # else:
        #     return HttpResponse("Data Not Inserted")
    else:
        form = EmpForm()
        return render(request,'emp_reg.html',{'form':form})
        # print(form.cleaned_data)
        # empname = form.cleaned_data.get('Employee Name')
        # email = form.cleaned_data.get('Email')
        # gender = form.cleaned_data.get('Gender')
        # status = form.cleaned_data.get('Status')
        # image = form.cleaned_data.get('Image')
        #
        # empdata = Employee(empname=empname,
        #           email=email,
        #           gender=gender,
        #           image=image,
        #           status=status)
        # empdata.save()

def emp_data(request):
    empdata = Employee.objects.all()
    return render(request,'emp_details.html',{'empdata':empdata})

def edit(request,id):
    empdata = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'empdata': empdata})


def update(request,id):
    empdata = Employee.objects.get(id=id)
    form = EmpForm(request.POST, instance=empdata)
    if form.is_valid():
        form.save()
        return redirect("emp")
    return render(request, 'edit.html', {'empdata': empdata})


def delete(request,id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()
    return redirect('emp')