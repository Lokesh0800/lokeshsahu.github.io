from distutils.log import error
from http.client import HTTPResponse
from tkinter import Entry
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import EmployeeData
import csv
import cv2
from django.utils.encoding import smart_str
# Create your views here.


def index(request):
    return render(request, 'home.html')


def entry_form(request):
    try:
        if request.method == "POST":
            Id = request.POST.get('Id')
            name = request.POST.get('name')
            desig = request.POST.get('desig')
            depart = request.POST.get('depart')
            doj = request.POST.get('doj')
            contact = request.POST.get('contact')
            ins = EmployeeData(
                Emp_id=Id, Emp_name=name, designation=desig, department=depart, doj=doj, contact=contact)
            ins.save()
            return HttpResponseRedirect("DataEntry")
        return render(request, 'Entry.html')

    except:
        messages.error(request,"Error!Missing Fields")
        return render(request, 'Entry.html')



def access_form(request):
    try:
        if request.method == 'POST':
            Id = request.POST.get('Id')
            data = EmployeeData.objects.get(Emp_id = Id)
            return render(request, 'Access.html',{"DATA":data} )
        else:
            return render(request, 'Access.html')
    except:
        return render(request, 'Access.html',{"text":"Error! Field is Empty or Given Id DoesNotExist"} )
            
    
def delete_form(request):
    try:
        if request.method == 'POST':
            Id = request.POST.get('Id') 
            data = EmployeeData.objects.get(Emp_id = Id)
            d2 = data
            data.delete()
            return render(request, 'Delete.html',{"DATA":d2,"Text":"has been deleted"})
    except:
        return render(request, 'Delete.html',{"text":"Error! Field is Empty or Given Id DoesNotExist"})
    return render(request, 'Delete.html')

def csv_convertion(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Emp_datasheet.csv"'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow([
		smart_str(u"Emp_id"),
		smart_str(u"Emp_name"),
		smart_str(u"Designation"),
		smart_str(u"Department"),
        smart_str(u"DOJ"),
        smart_str(u"Contact"),
	])
	events = EmployeeData.objects.all() 
	for event in events:
		writer.writerow([
			smart_str(event.Emp_id),
			smart_str(event.Emp_name),
			smart_str(event.designation),
			smart_str(event.department),
            smart_str(event.doj),
            smart_str(event.contact),
		])
	return response

def login(request):
    return render(request, 'login.html')
