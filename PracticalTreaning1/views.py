from http.client import HTTPResponse
from django.shortcuts import render
from model.models import Book,test
from django.http import HttpResponse
def book(request):
        list=test.objects.all()
        m=''
        if request.method=='POST':
            v_name=request.POST['f_name']
            v_email=request.POST['f_email']
            v_date=request.POST['f_date']
            v_time=request.POST['f_time']
            v_department=request.POST['f_appointmentfor']
            bk=Book(Name=v_name, Email=v_email, Date=v_date, Time=v_time, Department=v_department)
            bk.save()
            m="succeccfully booking"

        return render(request,'index.html',{'outpot':m,'tests':list})   